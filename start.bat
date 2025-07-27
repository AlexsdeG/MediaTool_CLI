@echo off
title MediaTool CLI

echo ====================================
echo      MediaTool CLI Launcher
echo ====================================
echo.

:: Check if virtual environment exists
if not exist "venv\Scripts\activate.bat" (
    echo ERROR: Virtual environment not found!
    echo Please run the following commands first:
    echo.
    echo   python -m venv venv
    echo   venv\Scripts\activate
    echo   pip install -r requirements.txt
    echo.
    pause
    exit /b 1
)

:: Check if main.py exists
if not exist "main.py" (
    echo ERROR: main.py not found!
    echo Make sure you're running this from the MediaTool_CLI directory.
    echo.
    pause
    exit /b 1
)

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Starting MediaTool CLI...
echo.
python main.py

echo.
echo MediaTool CLI has closed.
echo.
pause