#!/usr/bin/env python3
"""Portable, dependency-free catalogue integrity checks. Python 3.10+."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import sys
from urllib.parse import unquote, urlsplit

NAME = re.compile(r'(?=.{1,64}\Z)[a-z0-9]+(?:-[a-z0-9]+)*\Z')
LIMIT = 4 * 1024 * 1024


def safe(root, relative):
    if not isinstance(relative, str) or not relative or '\\' in relative or ':' in relative:
        raise ValueError('unsafe-path')
    parts = PurePosixPath(relative).parts
    if relative.startswith('/') or '..' in parts or (relative != '.gitignore' and any(p.startswith('.') for p in parts)):
        raise ValueError('unsafe-path')
    path = root
    for part in parts:
        path = path / part
        if path.is_symlink():
            raise ValueError('symlink')
    return path


def read(path):
    if path.stat().st_size > LIMIT:
        raise ValueError('oversized-file')
    return path.read_text(encoding='utf-8')


def metadata(text):
    if not text.startswith('---\n') or '\n---\n' not in text[4:]:
        raise ValueError('invalid-frontmatter')
    fields = {}
    for line in text[4:text.index('\n---\n', 4)].splitlines():
        if not line.strip():
            continue
        key, sep, value = line.partition(':')
        if not sep or key in fields or key.strip() != key:
            raise ValueError('invalid-frontmatter')
        value = value.strip()
        if value.startswith('"'):
            value = json.loads(value)
        elif value.startswith("'") and value.endswith("'"):
            value = value[1:-1].replace("''", "'")
        if not isinstance(value, str):
            raise ValueError('invalid-frontmatter')
        fields[key] = value
    return fields


def check(root):
    root = Path(root).resolve()
    errors = []
    try:
        if (root/'catalogue.json').is_symlink():
            return ['symlink: catalogue.json']
        doc = json.loads(read(root/'catalogue.json'))
        if doc.get('schema_version') != 1 or not isinstance(doc.get('files'), dict):
            return ['invalid-catalogue']
        for group in ('skills', 'personas', 'bundles'):
            names = doc.get(group)
            if not isinstance(names, list) or any(not isinstance(n,str) or not NAME.fullmatch(n) for n in names):
                return ['invalid-catalogue: '+group]
            if len(names) != len(set(names)):
                return ['duplicate-name: '+group]
        for rel, digest in doc['files'].items():
            try:
                p = safe(root, rel)
                if not p.is_file():
                    errors.append('missing-file: '+rel)
                elif not isinstance(digest,str) or not re.fullmatch('[0-9a-f]{64}',digest):
                    errors.append('invalid-digest: '+rel)
                elif p.stat().st_size > LIMIT:
                    errors.append('oversized-file: '+rel)
                elif hashlib.sha256(p.read_bytes()).hexdigest() != digest:
                    errors.append('hash-mismatch: '+rel)
            except ValueError as exc:
                errors.append(str(exc)+': '+rel)
        for p in root.rglob('*'):
            rel = p.relative_to(root).as_posix()
            if '.git' in p.relative_to(root).parts or '__pycache__' in p.relative_to(root).parts:
                continue
            if p.is_symlink():
                errors.append('symlink: '+rel)
            elif p.is_file() and rel != 'catalogue.json' and rel not in doc['files']:
                errors.append('unlisted-file: '+rel)
        if not (root/'LICENSE').is_file():
            errors.append('missing-licence: root')
        found = []
        for rel in doc['files']:
            try:
                p = safe(root, rel)
            except ValueError:
                continue
            if not p.is_file():
                continue
            if p.name == 'SKILL.md':
                text = read(p)
                try:
                    fields = metadata(text)
                    name = fields.get('name','')
                    if not NAME.fullmatch(name) or p.parent.name != name or rel != f'skills/{name}/SKILL.md':
                        errors.append('invalid-name: '+rel)
                    found.append(name)
                    if not fields.get('license'):
                        errors.append('missing-licence: '+rel)
                    if not fields.get('description'):
                        errors.append('missing-description: '+rel)
                    description = fields.get('description','')
                    if len(description) > 300 or '\n' in description or '\r' in description:
                        errors.append('invalid-description: '+rel)
                    if not text.split('\n---\n',1)[1].strip():
                        errors.append('empty-instructions: '+rel)
                    if not (p.parent/'LICENSE').is_file():
                        errors.append('missing-licence: '+rel)
                except (ValueError, TypeError) as exc:
                    errors.append('invalid-frontmatter: '+rel+' '+str(exc))
            if p.suffix == '.md':
                for target in re.findall(r'\]\(([^\s)]+)(?:\s+"[^"]*")?\)', read(p)):
                    parsed = urlsplit(target.strip('<>'))
                    if parsed.scheme or not parsed.path:
                        continue
                    q = (p.parent / unquote(parsed.path)).resolve()
                    if not q.is_relative_to(root) or not q.exists():
                        errors.append('missing-reference: '+rel+' -> '+target)
        if sorted(found) != sorted(doc['skills']):
            errors.append('skill-inventory-mismatch')
        for group, filename in [('personas','persona.json'),('bundles','bundle.json')]:
            present = sorted(p.parent.name for p in (root/group).glob('*/'+filename))
            if present != sorted(doc[group]):
                errors.append('package-inventory-mismatch: '+group)
            for name in doc[group]:
                manifest = safe(root,f'{group}/{name}/{filename}')
                if not manifest.is_file():
                    errors.append('missing-file: '+str(manifest.relative_to(root)))
                    continue
                pack = json.loads(read(manifest))
                members = pack.get('members')
                if (pack.get('name') != name or not isinstance(members,list) or not members
                    or any(not isinstance(member,str) for member in members)
                    or len(members) != len(set(members))):
                    errors.append('invalid-membership: '+name)
                    continue
                if group == 'personas' and not (manifest.parent/'PERSONA.md').is_file():
                    errors.append('missing-persona: '+name)
                for member in pack['members']:
                    if member not in doc['skills']:
                        errors.append('missing-member: '+name+' -> '+str(member))
    except (OSError, ValueError, TypeError, KeyError, AttributeError) as exc:
        errors.append('invalid-catalogue: '+str(exc))
    return sorted(set(errors))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors = check(args.root)
    print(json.dumps({'status':'fail' if errors else 'structural-pass', 'errors':errors,
                      'limit':'Integrity checks are not behavioural or licensing proof. Trust the release source; hashes are not signatures.'},indent=2))
    return 1 if errors else 0

if __name__ == '__main__':
    sys.exit(main())
