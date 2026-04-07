#!/bin/bash

echo "🚀 Starting Portfolio with AI Chatbot"
echo "======================================"
echo ""

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
NC='\033[0m' # No Color

# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

echo -e "${PURPLE}📂 Project Directory: $SCRIPT_DIR${NC}"
echo ""

# Function to cleanup on exit
cleanup() {
    echo ""
    echo "🛑 Stopping all services..."
    kill $ANGULAR_PID 2>/dev/null
    kill $PYTHON_PID 2>/dev/null
    echo "✅ All services stopped"
    exit 0
}

# Set up trap to cleanup on Ctrl+C
trap cleanup SIGINT SIGTERM

echo -e "${BLUE}Step 1/2: Starting Python ML Backend...${NC}"
echo "----------------------------------------"

# Start Python backend in background
cd "$SCRIPT_DIR/chatbot-backend"

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment and start backend
source venv/bin/activate

# Check if dependencies are installed
if [ ! -d "venv/lib/python"*"/site-packages/flask" ]; then
    echo "📚 Installing Python dependencies (first time only, 2-5 minutes)..."
    pip install --upgrade pip -q
    pip install -r requirements.txt -q
fi

echo "🤖 Starting Python backend on http://localhost:5000..."
python app.py > ../python-backend.log 2>&1 &
PYTHON_PID=$!

# Wait for Python backend to start
sleep 3

# Check if Python backend started successfully
if ps -p $PYTHON_PID > /dev/null; then
    echo -e "${GREEN}✅ Python backend started (PID: $PYTHON_PID)${NC}"
else
    echo "❌ Failed to start Python backend"
    echo "Check python-backend.log for errors"
    exit 1
fi

echo ""
echo -e "${BLUE}Step 2/2: Starting Angular Frontend...${NC}"
echo "---------------------------------------"

# Start Angular in background
cd "$SCRIPT_DIR"

# Check if node_modules exists
if [ ! -d "node_modules" ]; then
    echo "📦 Installing npm dependencies..."
    npm install
fi

echo "⚡ Starting Angular on http://localhost:4200..."
npm start > angular-frontend.log 2>&1 &
ANGULAR_PID=$!

# Wait for Angular to start
sleep 5

# Check if Angular started successfully
if ps -p $ANGULAR_PID > /dev/null; then
    echo -e "${GREEN}✅ Angular frontend started (PID: $ANGULAR_PID)${NC}"
else
    echo "❌ Failed to start Angular frontend"
    echo "Check angular-frontend.log for errors"
    kill $PYTHON_PID 2>/dev/null
    exit 1
fi

echo ""
echo "======================================"
echo -e "${GREEN}🎉 All Services Running!${NC}"
echo "======================================"
echo ""
echo -e "📊 Service Status:"
echo -e "  ${PURPLE}Python Backend:${NC}  http://localhost:5000 (PID: $PYTHON_PID)"
echo -e "  ${PURPLE}Angular Frontend:${NC} http://localhost:4200 (PID: $ANGULAR_PID)"
echo ""
echo -e "📝 Logs:"
echo "  Python:  tail -f python-backend.log"
echo "  Angular: tail -f angular-frontend.log"
echo ""
echo -e "🌐 Open your browser:"
echo -e "  ${BLUE}http://localhost:4200${NC}"
echo ""
echo -e "💬 Test AI Chatbot:"
echo "  1. Click the purple chat button (bottom-right)"
echo "  2. Ask: 'What is your experience?'"
echo "  3. Response should show (ML) tag"
echo ""
echo "⏹️  Press Ctrl+C to stop all services"
echo "======================================"
echo ""

# Keep script running and monitor processes
while true; do
    # Check if Python backend is still running
    if ! ps -p $PYTHON_PID > /dev/null; then
        echo "❌ Python backend stopped unexpectedly"
        cleanup
    fi
    
    # Check if Angular is still running
    if ! ps -p $ANGULAR_PID > /dev/null; then
        echo "❌ Angular frontend stopped unexpectedly"
        cleanup
    fi
    
    sleep 5
done
