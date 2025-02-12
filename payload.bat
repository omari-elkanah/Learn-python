Install-Module PSWindowsUpdate
Add-WUServiceManager -MicrosoftUpdate Y
Get-WindowsUpdate
Install-WindowsUpdate -MicrosoftUpdate -AcceptAll -AutoReboot
pause