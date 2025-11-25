Phyzioline React + TypeScript Frontend

Quick start (Windows PowerShell):

```powershell
cd "d:\\phyzio app 2.0\\phyzioline\\frontend-react"
npm install
npm run dev
```

The dev server runs on `http://localhost:3000` and proxies `/api` requests to `http://localhost:8000` (Django).

Where to edit:
- `src/pages/Accounts.tsx`, `src/pages/Marketplace.tsx`, `src/pages/Jobs.tsx`, `src/pages/Explore.tsx` — initial placeholders.
- `src/components/Header.tsx` — navigation and layout.
- `src/services/api.ts` — axios instance to call Django REST API.

Authentication:
- Store JWT `access` token in `localStorage` key `accessToken` to have the axios helper send `Authorization: Bearer <token>`.
