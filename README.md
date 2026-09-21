# Aurora Grand Hotel - AI Guest Assistant

Full-stack AI-powered hotel concierge built with React + FastAPI.

## How to Run

### Backend
cd hotel_guest_assistant/backend
pip install -r requirements.txt
uvicorn main:app --reload
Runs at http://localhost:8000

### Frontend
cd hotel_guest_assistant/frontend
npm install
npm run dev
Runs at http://localhost:5173

## Architecture
User -> React Chat UI -> FastAPI /chat API -> LLM Intent Detection -> JSON Knowledge Base + mock checkAvailability(checkIn, checkOut, adults) -> Structured Response -> Frontend

- Frontend: React/Vite, Chat interface with loading, error states
- Backend: FastAPI, handles context, validation, logging
- Data: data/hotel.json (rooms, policies, faqs)
- AI: LLM for understanding, deterministic logic for availability

## API Examples
curl -X POST http://localhost:8000/chat -H "Content-Type: application/json" -d '{"message":"What is check-in time?"}'
curl -X POST http://localhost:8000/chat -d '{"message":"Do you have rooms for 3 guests on 2026-10-10?","context":{"checkIn":"2026-10-10","checkOut":"2026-10-11","adults":3}}'

## AI Tools Used
- ChatGPT: Generated initial full-stack zip
- Meta AI: Fixed GitHub structure, Vercel errors, docs

## Demo
Local working. No deployment needed as per assignment optional.
