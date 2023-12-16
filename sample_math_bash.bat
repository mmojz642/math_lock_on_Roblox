@echo off
python "C:\path\to\math_problem.py"
if %ERRORLEVEL% == 0 (
	start "" "C:\path\to\Roblox\Versions\version-48a28da848b7420d\RobloxPlayerBeta.exe"
	echo.
	echo Please wait, Roblox is loading!
	echo.
) else (
	echo Try again!
)
timeout /t 3 /nobreak