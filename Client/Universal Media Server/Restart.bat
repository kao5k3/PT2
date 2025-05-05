@echo off
taskkill /IM javaw.exe /F
timeout /t 5 /nobreak >nul
start "" "C:\Program Files\Universal Media Server\UMS.exe"
