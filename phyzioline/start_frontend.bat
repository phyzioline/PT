@echo off
echo ========================================
echo   Starting Phyzioline Frontend (React)
echo ========================================
echo.

REM Navigate to frontend directory
cd frontend

echo [1/2] Installing dependencies...
call npm install
echo.

echo [2/2] Starting React development server...
echo.
echo Frontend running on: http://localhost:5173
echo.
echo Press Ctrl+C to stop the server
echo.

call npm run dev
