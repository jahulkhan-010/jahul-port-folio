#!/bin/bash

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
RED='\033[0;31m'
NC='\033[0m'

clear
echo ""
echo "═══════════════════════════════════════════════════════════"
echo -e "${PURPLE}   🚀 Jahul's Portfolio + AI Chatbot Launcher 🤖${NC}"
echo "═══════════════════════════════════════════════════════════"
echo ""

# Get script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Cleanup function
cleanup() {
    echo ""
    echo -e "${RED}🛑 Stopping all services...${NC}"
    kill $PYTHON_PID 2>/dev/null
    kill $ANGULAR_PID 2>/dev/null
    echo -e "${GREEN}✅ All services stopped${NC}"
    exit 0
}

trap cleanup SIGINT SIGTERM

# Start Python Backend
echo -e "${BLUE}[1/2] Starting Python ML Backend...${NC}"
echo "─────────────────────────────────────────────────────────"

cd "$SCRIPT_DIR/chatbot-backend"

# Setup virtual environment if needed
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

source venv/bin/activate

# Install dependencies if needed
if [ ! -f "venv/installed" ]; then
    echo "📚 Installing dependencies (first time, 2-5 mins)..."
    pip install --upgrade pip -q
    pip install -r requirements.txt -q
    touch venv/installed
fi

# Start Python backend
echo -e "${GREEN}🤖 Starting Python on http://localhost:5000${NC}"
python app.py &
PYTHON_PID=$!

sleep 3

# Verify Python started
if ! ps -p $PYTHON_PID > /dev/null; then
    echo -e "${RED}❌ Failed to start Python backend${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Python backend running (PID: $PYTHON_PID)${NC}"

# Start Angular Frontend
echo ""
echo -e "${BLUE}[2/2] Starting Angular Frontend...${NC}"
echo "─────────────────────────────────────────────────────────"

cd "$SCRIPT_DIR"

# Install npm dependencies if needed
if [ ! -d "node_modules" ]; then
    echo "📦 Installing npm dependencies..."
    npm install
fi

echo -e "${GREEN}⚡ Starting Angular on http://localhost:4200${NC}"
npm start &
ANGULAR_PID=$!

sleep 5

# Verify Angular started
if ! ps -p $ANGULAR_PID > /dev/null; then
    echo -e "${RED}❌ Failed to start Angular${NC}"
    kill $PYTHON_PID 2>/dev/null
    exit 1
fi

echo -e "${GREEN}✅ Angular frontend running (PID: $ANGULAR_PID)${NC}"

# All services started
echo ""
echo "═══════════════════════════════════════════════════════════"
echo -e "${GREEN}   🎉 ALL SERVICES RUNNING!${NC}"
echo "═══════════════════════════════════════════════════════════"
echo ""
echo -e "${PURPLE}📊 Services:${NC}"
echo -e "   ${BLUE}Python Backend:${NC}  http://localhost:5000"
echo -e "   ${BLUE}Angular App:${NC}     http://localhost:4200"
echo ""
echo -e "${PURPLE}🌐 Open in browser:${NC}"
echo -e "   ${GREEN}http://localhost:4200${NC}"
echo ""
echo -e "${PURPLE}💬 Test AI Chatbot:${NC}"
echo "   1. Click purple chat button (bottom-right)"
echo "   2. Ask: 'What is your experience?'"
echo "   3. Response should show (ML) tag"
echo ""
echo -e "${PURPLE}⏹️  Stop services:${NC}"
echo "   Press Ctrl+C in this terminal"
echo ""
echo "═══════════════════════════════════════════════════════════"
echo ""

# Auto-open browser (optional)
sleep 2
echo -e "${GREEN}🌐 Opening browser...${NC}"
if command -v open &> /dev/null; then
    open http://localhost:4200
elif command -v xdg-open &> /dev/null; then
    xdg-open http://localhost:4200
elif command -v start &> /dev/null; then
    start http://localhost:4200
fi

echo ""
echo "Monitoring services... (Press Ctrl+C to stop)"
echo ""

# Monitor processes
while true; do
    if ! ps -p $PYTHON_PID > /dev/null; then
        echo -e "${RED}❌ Python backend stopped${NC}"
        cleanup
    fi
    
    if ! ps -p $ANGULAR_PID > /dev/null; then
        echo -e "${RED}❌ Angular stopped${NC}"
        cleanup
    fi
    
    sleep 5
done
