#!/bin/bash

echo "🔍 Verifying Production Configuration"
echo "======================================"
echo ""

GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Check 1: environment.prod.ts has correct URL
echo "📋 Checking environment.prod.ts..."
if grep -q "cloudfunctions.net" src/environments/environment.prod.ts; then
    echo -e "${GREEN}✅ Production environment has Cloud Functions URL${NC}"
else
    echo -e "${RED}❌ Production environment missing Cloud Functions URL${NC}"
fi
echo ""

# Check 2: angular.json has fileReplacements
echo "📋 Checking angular.json..."
if grep -q "fileReplacements" angular.json; then
    echo -e "${GREEN}✅ fileReplacements configured in angular.json${NC}"
else
    echo -e "${RED}❌ fileReplacements missing in angular.json${NC}"
    echo -e "${YELLOW}   Add fileReplacements to use production environment!${NC}"
fi
echo ""

# Check 3: Build and verify
echo "📋 Building production to verify..."
npm run build:prod > /dev/null 2>&1

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Production build successful${NC}"
    
    # Check if dist contains localhost
    echo ""
    echo "📋 Checking built files for localhost..."
    if grep -r "localhost:5001" dist/jahul-port-folio/browser/ > /dev/null 2>&1; then
        echo -e "${RED}❌ WARNING: Built files still contain localhost:5001${NC}"
        echo -e "${YELLOW}   This means production environment is not being used!${NC}"
    else
        echo -e "${GREEN}✅ No localhost references in build${NC}"
    fi
    
    # Check if dist contains Cloud Functions URL
    echo ""
    echo "📋 Checking built files for Cloud Functions URL..."
    if grep -r "cloudfunctions.net" dist/jahul-port-folio/browser/ > /dev/null 2>&1; then
        echo -e "${GREEN}✅ Cloud Functions URL found in build${NC}"
    else
        echo -e "${YELLOW}⚠️  Cloud Functions URL not found in build${NC}"
    fi
else
    echo -e "${RED}❌ Production build failed${NC}"
fi

echo ""
echo "======================================"
echo "📊 Verification Summary"
echo "======================================"
echo ""
echo "If all checks passed:"
echo "  → Run: ./deploy.sh"
echo "  → Visit: https://angularwithjahul.web.app"
echo "  → Test chatbot"
echo ""
echo "If checks failed:"
echo "  → Review: FIX_PRODUCTION_URL.md"
echo "  → Fix issues and run this script again"
echo ""
