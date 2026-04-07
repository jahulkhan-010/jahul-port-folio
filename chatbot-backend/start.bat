@echo off
echo.
echo 🤖 AI Chatbot Backend Setup Script
echo ====================================
echo.

REM Check if virtual environment exists
if not exist "venv" (
    echo 📦 Creating virtual environment...
    python -m venv venv
    echo ✅ Virtual environment created!
) else (
    echo ✅ Virtual environment already exists
)

REM Activate virtual environment
echo 🔌 Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo 📚 Installing dependencies...
pip install --upgrade pip
pip install -r requirements.txt

echo.
echo ✅ Setup complete!
echo.
echo 🚀 Starting AI Chatbot Backend...
echo    Server: http://localhost:5000
echo    Health: http://localhost:5000/api/health
echo    CORS enabled for http://localhost:4200
echo.
echo    Press Ctrl+C to stop the server
echo ====================================
echo.

REM Run the Flask app
python app.py

pause
