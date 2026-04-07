@echo off
setlocal enabledelayedexpansion

echo.
echo ============================================
echo 🚀 Starting Portfolio with AI Chatbot
echo ============================================
echo.

REM Get current directory
set PROJECT_DIR=%~dp0

echo 📂 Project Directory: %PROJECT_DIR%
echo.

echo ============================================
echo Step 1/2: Starting Python ML Backend...
echo ============================================

REM Start Python backend in new window
cd /d "%PROJECT_DIR%chatbot-backend"

REM Check if virtual environment exists
if not exist "venv" (
    echo 📦 Creating virtual environment...
    python -m venv venv
)

REM Start Python in new window
start "Python ML Backend" cmd /k "venv\Scripts\activate && pip install -r requirements.txt && python app.py"

echo ✅ Python backend starting in new window...
echo    URL: http://localhost:5000
echo.

REM Wait for Python to start
timeout /t 5 /nobreak > nul

echo ============================================
echo Step 2/2: Starting Angular Frontend...
echo ============================================

REM Start Angular in new window
cd /d "%PROJECT_DIR%"

REM Check if node_modules exists
if not exist "node_modules" (
    echo 📦 Installing npm dependencies...
    call npm install
)

REM Start Angular in new window
start "Angular Frontend" cmd /k "npm start"

echo ✅ Angular frontend starting in new window...
echo    URL: http://localhost:4200
echo.

REM Wait for Angular to start
timeout /t 5 /nobreak > nul

echo ============================================
echo 🎉 All Services Started!
echo ============================================
echo.
echo 📊 Two new windows opened:
echo    1. Python ML Backend  - http://localhost:5000
echo    2. Angular Frontend   - http://localhost:4200
echo.
echo 🌐 Open your browser:
echo    http://localhost:4200
echo.
echo 💬 Test AI Chatbot:
echo    1. Click the purple chat button (bottom-right)
echo    2. Ask: "What is your experience?"
echo    3. Response should show (ML) tag
echo.
echo 📝 To stop services:
echo    Close both terminal windows or press Ctrl+C in each
echo.
echo ============================================
echo.

pause
