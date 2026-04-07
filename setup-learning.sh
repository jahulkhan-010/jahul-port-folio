#!/bin/bash

echo "🧠 Setting Up AI Learning Chatbot"
echo "=================================="
echo ""

GREEN='\033[0;32m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
NC='\033[0m'

# Step 1: Check Python backend
echo -e "${BLUE}Step 1/4: Checking Python Backend...${NC}"

if [ ! -d "chatbot-backend/venv" ]; then
    echo "📦 Creating Python virtual environment..."
    cd chatbot-backend
    python3 -m venv venv
    cd ..
fi

echo -e "${GREEN}✅ Python environment ready${NC}"
echo ""

# Step 2: Install Python dependencies
echo -e "${BLUE}Step 2/4: Installing Dependencies...${NC}"

cd chatbot-backend
source venv/bin/activate
pip install flask --quiet

echo -e "${GREEN}✅ Dependencies installed${NC}"
echo ""

# Step 3: Check Firebase setup
echo -e "${BLUE}Step 3/4: Checking Firebase Setup...${NC}"

if ! command -v firebase &> /dev/null; then
    echo "⚠️  Firebase CLI not found"
    echo "Install with: npm install -g firebase-tools"
else
    echo -e "${GREEN}✅ Firebase CLI installed${NC}"
fi

cd ..
echo ""

# Step 4: Install npm dependencies
echo -e "${BLUE}Step 4/4: Checking NPM Dependencies...${NC}"

if [ ! -d "node_modules" ]; then
    echo "📦 Installing npm packages..."
    npm install
else
    echo -e "${GREEN}✅ NPM packages ready${NC}"
fi

echo ""
echo "=================================="
echo -e "${GREEN}🎉 Setup Complete!${NC}"
echo "=================================="
echo ""
echo "📋 Next Steps:"
echo ""
echo "🔹 Development Mode:"
echo "   npm run dev"
echo "   Then: http://localhost:4200"
echo ""
echo "🔹 Admin Panel (Manage Learning):"
echo "   cd chatbot-backend"
echo "   python admin_panel.py"
echo ""
echo "🔹 Production Deploy:"
echo "   ./deploy.sh"
echo ""
echo "🔹 Documentation:"
echo "   • AI_LEARNING_CHATBOT.md - Learning features"
echo "   • AI_LEARNING_DEV_AND_PROD.md - Dev & Prod setup"
echo "   • PRODUCTION_READY.md - Deployment guide"
echo ""
echo "=================================="
echo -e "${PURPLE}Your AI Learning Chatbot is Ready! 🧠${NC}"
echo "=================================="
