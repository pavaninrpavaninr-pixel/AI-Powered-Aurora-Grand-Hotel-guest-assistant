# Aurora Grand Hotel Guest Assistant

Full-stack React + FastAPI assignment implementation.

## Requirements
- Python 3.10+
- Node.js 18+

## Run backend (VS Code terminal 1)
```bash
cd backend
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

## Run frontend (VS Code terminal 2)
```bash
cd frontend
npm install
npm run dev
```
Open the URL shown by Vite, normally http://localhost:5173.

## Tests
```bash
cd backend
pytest
```

## Architecture
React frontend calls FastAPI; FastAPI uses a JSON knowledge base for deterministic FAQs and a deterministic availability function. No API key is required. Unsupported questions receive a safe fallback rather than an invented answer.

## Evaluation scenarios
1. Check-in question
2. Check-out question
3. Pool question
4. Breakfast question
5. Cancellation policy
6. Three-guest room recommendation
7. Unsupported amenity fallback
8. Availability with valid dates
9. Availability with invalid dates
10. Frontend/backend connection failure message

## Production improvements
Add authentication, database-backed inventory, real booking integration, monitoring, rate limiting, stronger validation, multilingual support, and an optional grounded LLM with citations/retrieval.
