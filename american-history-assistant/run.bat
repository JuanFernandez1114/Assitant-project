@echo off
REM AI-Powered FAQ Helpdesk - Quick Start Script for Windows

echo ==========================================
echo AI-Powered FAQ Helpdesk
echo ==========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH.
    echo Please install Python 3.7 or higher from https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [OK] Python found
echo.

REM Check if virtual environment exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
    echo [OK] Virtual environment created
    echo.
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat
echo [OK] Virtual environment activated
echo.

REM Check if requirements are installed
python -c "import flask, pandas, sklearn" >nul 2>&1
if errorlevel 1 (
    echo Installing required packages...
    pip install -r requirements.txt
    echo [OK] Dependencies installed
    echo.
) else (
    echo [OK] Dependencies already installed
    echo.
)

REM Check if data file exists
if not exist "data\faq_data.csv" (
    echo [ERROR] FAQ data file not found at data\faq_data.csv
    pause
    exit /b 1
)

echo [OK] FAQ data file found
echo.

REM Start the Flask application
echo ==========================================
echo Starting Flask server...
echo ==========================================
echo.
echo Open your browser and go to:
echo    http://127.0.0.1:5000
echo.
echo Press Ctrl+C to stop the server
echo.

python app.py

pause

