#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")"

if [[ ! -f node_modules/.bin/wrangler ]]; then
  npm install
fi

npm run build
npm run check

echo "Deploying Antigua Shore Excursion World 2.0 to Cloudflare..."
npx wrangler deploy

echo "Done. Check https://antiguashoreexcursion.com/"
