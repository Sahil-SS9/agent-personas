@echo off
setlocal enabledelayedexpansion
REM kill-port-8001.bat — Kill any zombie process on port 8001 and verify it's free.
REM Usage:  Double-click or run from terminal.
REM         Returns exit code 0 if port was freed, 1 if already free, 2 on error.

set "PORT=8001"

echo [ACE-Step] Checking port %PORT%...
netstat -ano | findstr ":%PORT% " >nul 2>&1
if !ERRORLEVEL! NEQ 0 (
    echo [ACE-Step] Port %PORT% is already free.
    exit /b 1
)

echo [ACE-Step] Port %PORT% is in use. Finding the process...
for /f "tokens=5" %%p in ('netstat -ano ^| findstr ":%PORT% "') do (
    echo [ACE-Step] Killing PID: %%p
    powershell -Command "Stop-Process -Id %%p -Force" >nul 2>&1
    if !ERRORLEVEL! EQU 0 (
        echo [ACE-Step] Killed PID %%p
    ) else (
        echo [ACE-Step] Failed to kill PID %%p — try running as Administrator
    )
)

REM Small delay for process cleanup
ping 127.0.0.1 -n 2 >nul

REM Verify it's free now
netstat -ano | findstr ":%PORT% " >nul 2>&1
if !ERRORLEVEL! EQU 0 (
    echo [ACE-Step] FAILED: Port %PORT% is still in use.
    echo [ACE-Step] Try: powershell -Command "Stop-Process -Id (netstat -ano ^| findstr :%PORT% ^| findstr LISTENING ^| %%^^^$($_.Trim().Split()[-1])^) -Force"
    exit /b 2
)

echo [ACE-Step] Port %PORT% is now free. Ready to start the server.
exit /b 0
