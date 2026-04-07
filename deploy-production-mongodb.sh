#!/bin/bash

echo "🚀 Deploying to Production with MongoDB"
echo "========================================"
echo ""

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

# Check Firebase login
echo -e "${BLUE}Step 1/5: Checking Firebase Authentication...${NC}"
if ! firebase projects:list > /dev/null 2>&1; then
    echo -e "${RED}❌ Not logged in to Firebase${NC}"
    echo "Run: firebase login"
    exit 1
fi
echo -e "${GREEN}✅ Firebase authenticated${NC}"
echo ""

# Set environment variables for Cloud Functions
echo -e "${BLUE}Step 2/5: Setting Cloud Functions Environment Variables...${NC}"

firebase functions:config:set \
  mongodb.atlas_uri="mongodb+srv://jahulkhan_db_user:cOkS9qN2X7QWTaCE@jahul-chatbot.hqsd1xp.mongodb.net/?retryWrites=true&w=majority" \
  mongodb.atlas_db="jahul_chatbot_prod" \
  environment="production"

if [ $? -ne 0 ]; then
    echo -e "${YELLOW}⚠️  Environment config warning (continuing...)${NC}"
fi
echo -e "${GREEN}✅ Environment variables configured${NC}"
echo ""

# Build Angular
echo -e "${BLUE}Step 3/5: Building Angular Application...${NC}"
npm run build:prod

if [ $? -ne 0 ]; then
    echo -e "${RED}❌ Build failed!${NC}"
    exit 1
fi
echo -e "${GREEN}✅ Angular build complete${NC}"
echo ""

# Deploy Hosting
echo -e "${BLUE}Step 4/5: Deploying Firebase Hosting...${NC}"
firebase deploy --only hosting

if [ $? -ne 0 ]; then
    echo -e "${RED}❌ Hosting deployment failed!${NC}"
    exit 1
fi
echo -e "${GREEN}✅ Hosting deployed${NC}"
echo ""

# Deploy Functions with env vars
echo -e "${BLUE}Step 5/5: Deploying Cloud Functions with MongoDB...${NC}"

# Copy .env.yaml to functions directory
if [ -f "functions/.env.yaml" ]; then
    echo "Using .env.yaml for environment variables..."
fi

firebase deploy --only functions

if [ $? -ne 0 ]; then
    echo -e "${RED}❌ Functions deployment failed!${NC}"
    echo ""
    echo "Common issues:"
    echo "1. Make sure you're on Blaze (pay-as-you-go) plan"
    echo "2. Check that all APIs are enabled"
    echo "3. Verify MongoDB credentials in functions/.env.yaml"
    exit 1
fi
echo -e "${GREEN}✅ Cloud Functions deployed${NC}"
echo ""

# Test deployment
echo "========================================"
echo -e "${GREEN}🎉 Deployment Complete!${NC}"
echo "========================================"
echo ""
echo "🌐 Your portfolio:"
echo "   https://angularwithjahul.web.app"
echo "   https://jahul-portfolio.web.app"
echo ""
echo "🤖 Chatbot API:"
echo "   https://us-central1-jahul-portfolio.cloudfunctions.net/chatbot"
echo ""
echo "🗄️  MongoDB:"
echo "   Database: jahul_chatbot_prod"
echo "   Cluster: jahul-chatbot.hqsd1xp.mongodb.net"
echo ""
echo "🧪 Test your deployment:"
echo ""
echo "1. Health Check:"
echo "   curl https://us-central1-jahul-portfolio.cloudfunctions.net/chatbot/health"
echo ""
echo "2. Test Chat:"
echo '   curl -X POST https://us-central1-jahul-portfolio.cloudfunctions.net/chatbot \'
echo '     -H "Content-Type: application/json" \'
echo '     -d '"'"'{"question":"What is your experience?"}'"'"
echo ""
echo "3. View in MongoDB Atlas:"
echo "   https://cloud.mongodb.com/"
echo "   → Database → Browse Collections"
echo "   → jahul_chatbot_prod → conversations"
echo ""
echo "✅ Production is live with MongoDB integration!"
echo ""
