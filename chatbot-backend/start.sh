#!/bin/bash

echo "🤖 AI Chatbot Backend Setup Script"
echo "===================================="
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
    echo "✅ Virtual environment created!"
else
    echo "✅ Virtual environment already exists"
fi

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source venv/bin/activate

# Check if dependencies are installed
if [ ! -f "venv/lib/python*/site-packages/flask/__init__.py" ]; then
    echo "📚 Installing dependencies (this may take 2-5 minutes)..."
    pip install --upgrade pip
    pip install -r requirements.txt
    echo "✅ Dependencies installed!"
else
    echo "✅ Dependencies already installed"
fi

echo ""
echo "✅ Setup complete!"
echo ""
echo "🚀 Starting AI Chatbot Backend..."
echo "   Server: http://localhost:5000"
echo "   Health: http://localhost:5000/api/health"
echo "   CORS enabled for http://localhost:4200"
echo ""
echo "   Press Ctrl+C to stop the server"
echo "===================================="
echo ""

# Run the Flask app
python app.py
