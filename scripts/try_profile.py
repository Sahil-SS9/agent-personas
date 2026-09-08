#!/usr/bin/env python3
"""Stage a selected package in a NEW workspace; optionally run your own agent CLI."""
import argparse
import json
import os
from pathlib import Path
import queue
import re
import shutil
import signal
import subprocess
import sys
import threading
import time
from verify import check, NAME

PATHS = {'codex':'.agents/skills','claude':'.claude/skills','hermes':'hermes-home/skills',
         'openclaw':'.agents/skills','commandcode':'.commandcode/skills','pi':'.pi/skills','opencode':'.opencode/skills'}


def stage(root, selection, harness, dest):
    root, dest = Path(root).resolve(), Path(dest).absolute()
    if dest.resolve().is_relative_to(root):
        raise ValueError('destination must be outside the release source')
    if dest.exists() or dest.is_symlink():
        raise ValueError('destination exists; choose a new workspace')
    if any(p.is_symlink() for p in [dest.parent, *dest.parents]):
        raise ValueError('symlink destination ancestor')
    errors=check(root)
    if errors:
        raise ValueError('catalogue verification failed: '+str(errors[:5]))
    kind,sep,name=selection.partition(':')
    if not sep or not NAME.fullmatch(name) or harness not in PATHS:
        raise ValueError('invalid selection or harness')
    catalogue=json.loads((root/'catalogue.json').read_text())
    group={'skill':'skills','persona':'personas','bundle':'bundles'}.get(kind)
    if not group or name not in catalogue[group]:
        raise ValueError('unknown selection')
    if kind=='skill':members=[name]
    else:members=json.loads((root/group/name/(kind+'.json')).read_text())['members']
    dest.mkdir(parents=True,exist_ok=False)
    for member in members:
        shutil.copytree(root/'skills'/member,dest/PATHS[harness]/member)
    if kind=='persona':shutil.copyfile(root/'personas'/name/'PERSONA.md',dest/'PERSONA.md')
    receipt={'selection':selection,'harness':harness,'members':members,'skill_root':PATHS[harness],
             'native_loading':'unverified','behaviour':'unreviewed','isolation':'separate working directory only; not a security sandbox'}
    (dest/'staging.json').write_text(json.dumps(receipt,indent=2)+'\n')
    return receipt


def run_cli(command, prompt, cwd, allow=False, timeout=30, limit=262144):
    base={'native_loading':'unverified','behaviour':'unreviewed','output':''}
    if not allow:return dict(base,status='not-run')
    if not isinstance(command,list) or not command or any(not isinstance(x,str) or '\0' in x for x in command):
        raise ValueError('command must be a nonempty JSON argument array')
    if not 0 < timeout <= 600 or not 1 <= limit <= 1048576:
        raise ValueError('invalid timeout or output limit')
    # Arguments are passed literally. No shell, command concatenation or credential copying.
    args=[x.replace('{prompt}',prompt) for x in command]
    env={k:v for k,v in os.environ.items() if k in {'PATH','HOME','USERPROFILE','SYSTEMROOT','WINDIR','TEMP','TMP','LANG','LC_ALL','TERM','SSL_CERT_FILE','SSL_CERT_DIR'}}
    try:
        proc=subprocess.Popen(args,cwd=cwd,env=env,stdin=subprocess.DEVNULL,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,start_new_session=(os.name=='posix'))
    except OSError as exc:return dict(base,status='blocked',error=str(exc))
    chunks=queue.Queue(maxsize=8);stop=threading.Event()
    def drain():
        try:
            while not stop.is_set():
                data=proc.stdout.read1(4096)
                while not stop.is_set():
                    try:chunks.put(data,timeout=.05);break
                    except queue.Full:pass
                if not data:break
        finally:
            proc.stdout.close()
    reader=threading.Thread(target=drain,daemon=True);reader.start()
    output=bytearray();deadline=time.monotonic()+timeout;status=None
    while status is None:
        if time.monotonic()>=deadline:status='timeout';break
        try:data=chunks.get(timeout=min(.05,max(.001,deadline-time.monotonic())))
        except queue.Empty:continue
        if not data:break
        if len(output)+len(data)>limit:
            output.extend(data[:limit-len(output)]);status='output-limit';break
        output.extend(data)
    if status:
        try:
            if os.name=='posix':os.killpg(proc.pid,signal.SIGKILL)
            else:proc.kill()
        except ProcessLookupError:pass
    try:proc.wait(timeout=max(.01,deadline-time.monotonic()))
    except subprocess.TimeoutExpired:
        status='timeout'
        try:
            if os.name=='posix':os.killpg(proc.pid,signal.SIGKILL)
            else:proc.kill()
        except ProcessLookupError:pass
        proc.wait(timeout=2)
    stop.set();reader.join(timeout=1)
    text=output.decode('utf-8',errors='replace')
    text=re.sub(r'(?i)(bearer\s+)[A-Za-z0-9._-]+',r'\1[REDACTED]',text)
    text=re.sub(r'\bsk-[A-Za-z0-9_-]{12,}', '[REDACTED]',text)
    return dict(base,status=status or ('process-completed' if proc.returncode==0 else 'failed'),exit_code=proc.returncode,output=text)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1])
    p.add_argument('--select',required=True,help='skill:name, persona:name or bundle:name')
    p.add_argument('--harness',required=True,choices=PATHS)
    p.add_argument('--dest',required=True,type=Path,help='New directory only; existing paths are never overwritten')
    p.add_argument('--command-json',help='CLI argv array; {prompt} is replaced literally in an argument')
    p.add_argument('--prompt-file',type=Path)
    p.add_argument('--allow-execution',action='store_true')
    p.add_argument('--acknowledge-unsandboxed',action='store_true')
    p.add_argument('--timeout',type=float,default=120)
    a=p.parse_args()
    try:
        if a.allow_execution and (not a.acknowledge_unsandboxed or not a.command_json):
            raise ValueError('Execution may incur costs and access your account: provide a command and --acknowledge-unsandboxed. Configure sandboxing in your CLI.')
        prompt=a.prompt_file.read_text() if a.prompt_file else 'Read PERSONA.md if present, then use the selected installed skills on the supplied task. State missing inputs rather than inventing evidence. Do not make external changes.'
        if len(prompt)>65536:raise ValueError('prompt too large')
        command=json.loads(a.command_json) if a.command_json else None
        if a.allow_execution and (not isinstance(command,list) or not command or any(not isinstance(x,str) for x in command)):
            raise ValueError('command must be a nonempty argument array')
        receipt=stage(a.root,a.select,a.harness,a.dest)
        print(json.dumps({'staging':receipt},indent=2))
        if a.command_json:
            result=run_cli(command,prompt,a.dest,allow=a.allow_execution,timeout=a.timeout)
            print(json.dumps({'run':result},indent=2))
            return 0 if result['status'] in ('not-run','process-completed') else 1
        return 0
    except (OSError,ValueError,KeyError) as exc:
        print(json.dumps({'status':'blocked','error':str(exc)}));return 1

if __name__=='__main__':sys.exit(main())
