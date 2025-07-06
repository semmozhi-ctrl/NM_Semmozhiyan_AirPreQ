@echo off
title AirPreQ - Advanced Air Quality Intelligence
color 0A

echo.
echo ========================================
echo   AIRPREQ - MODERN UI/UX WEBSITE
echo ========================================
echo.
echo Starting AirPreQ with new design...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    echo Please install Python and try again
    pause
    exit /b 1
)

REM Install dependencies if needed
echo 📦 Checking dependencies...
pip install -r requirements.txt >nul 2>&1

REM Run the application
echo 🚀 Starting AirPreQ server...
echo.
echo ✨ New Features:
echo    - Modern dark theme with gradients
echo    - Glass morphism effects
echo    - Interactive animations
echo    - Mobile-responsive design
echo    - Enhanced visualizations
echo.
echo 🌐 Open your browser and go to: http://127.0.0.1:5000
echo ⏹️  Press Ctrl+C to stop the server
echo.

python run_airpreq.py

pause
