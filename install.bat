@echo off
echo Setting up The Alien Instruction Guide AI system...

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python and try again.
    exit /b 1
)

REM Check if pip is installed
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo pip is not installed. Please install pip and try again.
    exit /b 1
)

REM Create virtual environment
echo Creating virtual environment...
python -m venv venv

REM Activate virtual environment and install dependencies
echo Installing dependencies...
call venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt

REM Create necessary directories
echo Creating necessary directories...
mkdir ai\trained_model 2>nul
mkdir ai\training_data 2>nul

echo Installation complete! To activate the environment, run:
echo venv\Scripts\activate.bat
echo.
echo To train the model, run:
echo python ai\train_model.py 