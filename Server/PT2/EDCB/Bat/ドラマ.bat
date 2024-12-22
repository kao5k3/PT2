@echo off

set y=%date:~2,2%
set m=%date:~5,2%
setlocal ENABLEDELAYEDEXPANSION
set q=“~
if %m%==04 (
	set q=t
) else if %m%==05 (
	set q=t
) else if %m%==06 (
	set q=t
) else if %m%==07 (
	set q=‰Ä
) else if %m%==08 (
	set q=‰Ä
) else if %m%==09 (
	set q=‰Ä
) else if %m%==10 (
	set q=H
) else if %m%==11 (
	set q=H
) else if %m%==12 (
	set q=H
)
C:\PT2\EDCB\Bat\RecPost.py -f "$FilePath$" -g "ƒhƒ‰ƒ}" -a "!y!”N!q!" -s
ENDLOCAL
