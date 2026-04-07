#!/bin/bash

echo "🚀 Deploying Jahul's Portfolio to Firebase"
echo "=========================================="
echo ""

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m'

# Step 1: Build Angular App
echo -e "${BLUE}Step 1/3: Building Angular Application...${NC}"
echo "Running: npm run build"
npm run build --configuration production

if [ $? -ne 0 ]; then
    echo -e "${RED}❌ Build failed!${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Angular build complete!${NC}"
echo ""

# Step 2: Deploy Firebase Hosting
echo -e "${BLUE}Step 2/3: Deploying to Firebase Hosting...${NC}"
firebase deploy --only hosting

if [ $? -ne 0 ]; then
    echo -e "${RED}❌ Hosting deployment failed!${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Hosting deployed!${NC}"
echo ""

# Step 3: Deploy Cloud Functions
echo -e "${BLUE}Step 3/3: Deploying Cloud Functions...${NC}"
firebase deploy --only functions

if [ $? -ne 0 ]; then
    echo -e "${RED}❌ Functions deployment failed!${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Functions deployed!${NC}"
echo ""

echo "=========================================="
echo -e "${GREEN}🎉 Deployment Complete!${NC}"
echo "=========================================="
echo ""
echo "🌐 Your portfolio is live at:"
echo "   https://angularwithjahul.web.app"
echo "   https://jahul-portfolio.web.app"
echo ""
echo "🤖 Chatbot API endpoint:"
echo "   https://us-central1-jahul-portfolio.cloudfunctions.net/chatbot"
echo ""
echo "🧪 Test chatbot:"
echo "   1. Visit: https://angularwithjahul.web.app"
echo "   2. Click chat button"
echo "   3. Ask: 'What is your experience?'"
echo "   4. Open console (F12) - should NOT see localhost errors!"
echo ""
echo "✅ All done! Your site is now production-ready!"
echo ""
