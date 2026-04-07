#!/bin/bash

echo "🚀 Deploying Cloud Functions (Backend Only)"
echo "==========================================="
echo ""

GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${BLUE}Deploying Python Cloud Functions...${NC}"
firebase deploy --only functions

if [ $? -ne 0 ]; then
    echo -e "${RED}❌ Deployment failed!${NC}"
    exit 1
fi

echo ""
echo "==========================================="
echo -e "${GREEN}🎉 Cloud Functions Deployed!${NC}"
echo "==========================================="
echo ""
echo "🤖 Chatbot API:"
echo "   https://us-central1-jahul-portfolio.cloudfunctions.net/chatbot"
echo ""
echo "🧪 Test it:"
echo "   curl https://us-central1-jahul-portfolio.cloudfunctions.net/chatbot/health"
echo ""
echo "✅ All users will now get proper responses!"
echo ""
