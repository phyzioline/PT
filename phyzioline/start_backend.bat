@echo off
echo ========================================
echo   Starting Phyzioline Backend (Django)
echo ========================================
echo.

REM Activate virtual environment
call env\Scripts\activate.bat

echo [1/3] Virtual environment activated
echo.

REM Install dependencies if needed
echo [2/3] Checking dependencies...
pip install -q -r requirements.txt
echo.

REM Start Django server
echo [3/3] Starting Django server...
echo.
echo Backend running on: http://localhost:8000
echo Admin panel: http://localhost:8000/admin
echo API Documentation: http://localhost:8000/api/v1/
echo.
echo Press Ctrl+C to stop the server
echo.

python manage.py runserver
