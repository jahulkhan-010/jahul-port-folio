#!/bin/bash

echo "🗄️ Setting Up MongoDB for AI Chatbot"
echo "======================================"
echo ""

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

# Check if MongoDB is installed
echo -e "${BLUE}Step 1: Checking MongoDB Installation...${NC}"

if command -v mongod &> /dev/null; then
    echo -e "${GREEN}✅ MongoDB is installed${NC}"
    mongod --version | head -n 1
else
    echo -e "${YELLOW}⚠️  MongoDB not found${NC}"
    echo ""
    echo "Install MongoDB with:"
    echo "  brew tap mongodb/brew"
    echo "  brew install mongodb-community@7.0"
    echo "  brew services start mongodb-community@7.0"
    exit 1
fi

# Check if MongoDB is running
echo ""
echo -e "${BLUE}Step 2: Checking MongoDB Service...${NC}"

if pgrep -x "mongod" > /dev/null; then
    echo -e "${GREEN}✅ MongoDB is running${NC}"
else
    echo -e "${YELLOW}⚠️  MongoDB is not running${NC}"
    echo "Starting MongoDB..."
    brew services start mongodb-community@7.0
    sleep 2
    
    if pgrep -x "mongod" > /dev/null; then
        echo -e "${GREEN}✅ MongoDB started successfully${NC}"
    else
        echo -e "${RED}❌ Failed to start MongoDB${NC}"
        exit 1
    fi
fi

# Install Python dependencies
echo ""
echo -e "${BLUE}Step 3: Installing Python Dependencies...${NC}"

cd chatbot-backend

if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

source venv/bin/activate
pip install -q pymongo python-dotenv

echo -e "${GREEN}✅ Python dependencies installed${NC}"

# Check .env file
echo ""
echo -e "${BLUE}Step 4: Checking Configuration...${NC}"

if [ -f ".env" ]; then
    echo -e "${GREEN}✅ .env file exists${NC}"
else
    echo -e "${YELLOW}⚠️  Creating .env file...${NC}"
    cat > .env << 'EOF'
# MongoDB Configuration

# Local Development
MONGODB_LOCAL_URI=mongodb://localhost:27017/
MONGODB_LOCAL_DB=jahul_chatbot

# Production (MongoDB Atlas)
# Replace <password> with your actual password from MongoDB Atlas
MONGODB_ATLAS_URI=mongodb+srv://jahul-admin:<password>@jahul-chatbot.xxxxx.mongodb.net/?retryWrites=true&w=majority
MONGODB_ATLAS_DB=jahul_chatbot_prod

# Environment
ENVIRONMENT=development
EOF
    echo -e "${GREEN}✅ Created .env file${NC}"
    echo -e "${YELLOW}⚠️  Remember to update MongoDB Atlas credentials in .env!${NC}"
fi

# Test MongoDB connection
echo ""
echo -e "${BLUE}Step 5: Testing MongoDB Connection...${NC}"

python3 << 'PYTHON_CODE'
from pymongo import MongoClient
try:
    client = MongoClient('mongodb://localhost:27017/', serverSelectionTimeoutMS=2000)
    client.admin.command('ping')
    print("✅ MongoDB connection successful!")
    client.close()
except Exception as e:
    print(f"❌ MongoDB connection failed: {e}")
    exit(1)
PYTHON_CODE

if [ $? -eq 0 ]; then
    echo -e "${GREEN}MongoDB is ready!${NC}"
else
    echo -e "${RED}MongoDB connection test failed${NC}"
    exit 1
fi

cd ..

# Summary
echo ""
echo "======================================"
echo -e "${GREEN}✅ MongoDB Setup Complete!${NC}"
echo "======================================"
echo ""
echo "📋 Next Steps:"
echo ""
echo "1. Start MongoDB-integrated backend:"
echo "   cd chatbot-backend"
echo "   source venv/bin/activate"
echo "   python app_mongodb.py"
echo ""
echo "2. (Optional) Set up MongoDB Atlas for production:"
echo "   - Visit: https://www.mongodb.com/cloud/atlas/register"
echo "   - Create free M0 cluster"
echo "   - Update chatbot-backend/.env with Atlas credentials"
echo "   - See: MONGODB_SETUP_GUIDE.md"
echo ""
echo "3. Test locally:"
echo "   curl http://localhost:5001/api/health"
echo ""
echo "======================================"
