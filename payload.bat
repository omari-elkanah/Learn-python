@echo off
set logFile=%~dp0updateLog.txt
echo Checking for UsoClient... > %logFile%

:: Check if UsoClient is already installed
where UsoClient >nul 2>&1
if %errorlevel%==0 (
    echo UsoClient is already installed. >> %logFile%
) else (
    echo UsoClient is not found. It should be included in Windows 10 and later.
    echo Please ensure your system is running Windows 10 or later and has the latest updates.
    pause
    exit /b 1
)

echo Initiating Windows Update using UsoClient...

UsoClient ScanInstallWait >> %logFile%



echo Displaying available updates...
powershell -Command "Get-WindowsUpdateLog | Select-String -Pattern 'Title'" >> %logFile%
echo Updates have been initiated.

:: Optional: Open Windows Update settings
start ms-settings:windowsupdate 

pause
