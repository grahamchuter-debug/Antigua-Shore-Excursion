# Antigua Shore Excursion

World 2.0 cruise-passenger planning guide for St John's, Antigua.

## Canonical URL policy (Phase 15B)

- Host: `https://antiguashoreexcursion.com` (apex)
- Path form: **trailing-slash extensionless** (e.g. `/classic-beach-day/`)
- `.html` and bare extensionless paths **301** to the canonical form
- `www` **301** to matching apex path
- Query strings preserved

## Development

```bash
npm install
npm run build
npm run check
npm run preview
```

Open http://localhost:8907

## Deploy

```bash
npm run deploy
```

Public contact: hello@antiguashoreexcursion.com

Commerce, schedules, and CT-2 are out of scope for Phase 15B.
