@echo off
REM Ensure the batch file is run as administrator
whoami /groups | find "S-1-16-12288" >nul || (
    echo This batch file must be run as administrator!
    pause
    exit /b
)

REM Start Redis server
REM Replace <REDIS_PATH> with the path to the folder where Redis is installed.
REM Example: C:\Program Files (x86)\Redis
echo Starting Redis server...
start "Redis-Server" cmd /c "cd /d <REDIS_PATH> && redis-server redis.windows.conf"

REM Start Python server
REM Replace <PYTHON_SERVER_PATH> with the path to the folder containing your Python server.
REM Example: C:\Users\YourUsername\YourProject\Backend
echo Starting Python server...
start "Python-Server" cmd /c "cd /d <PYTHON_SERVER_PATH> && python run.py"

REM Start Frontend
REM Replace <FRONTEND_PATH> with the path to the folder containing your frontend project.
REM Example: C:\Users\YourUsername\YourProject\Frontend
echo Starting Frontend...
start "Frontend" cmd /c "cd /d <FRONTEND_PATH> && npm run dev"

REM Wait for 4 seconds to ensure the Frontend server has started
timeout /t 4 /nobreak >nul

REM Open the browser with the frontend URL
REM Replace <IP_With_PORT:5000> with your local IP-ADDRESS in you network and us the right port "5000".
REM Example: http://192.168.2.1:5000/
echo Opening browser to <IP_With_PORT:5000>...
start <IP_With_PORT:5000>


REM Wait for user input to stop all processes
echo All servers have been started. Press any key to stop all processes.
pause

REM Stop all processes
echo Stopping all processes...

REM Close Redis server window
taskkill /FI "WINDOWTITLE eq Redis-Server" /T /F

REM Delete all PNG files in the qr_codes folder before stopping the Python server
REM Replace <QR_CODES_PATH> with the path to the qr_codes folder.
REM Example: C:\Users\YourUsername\YourProject\Backend\qr_codes
echo Deleting PNG files in qr_codes folder...
del /q "<QR_CODES_PATH>\*.png"

REM Close Python server window
taskkill /FI "WINDOWTITLE eq Python-Server" /T /F

REM Close Frontend window with additional automation for npm
echo Stopping Frontend...
tasklist | find "node" >nul && (
    echo y | taskkill /IM "node.exe" /T /F
)
taskkill /FI "WINDOWTITLE eq Frontend" /T /F

echo All processes have been stopped.
pause
exit
