# Aurora Grand Hotel - Guest Assistant

AI-powered hotel chatbot using FastAPI + React + RAG

## 🚀 Live Demo Proof
Backend and Frontend both working perfectly!

### Chatbot answering:
- "what time is check-in?" -> "Check-in starts at 2:00 PM"
- "Do you have a swimming pool?" -> "outdoor pool open 6 AM to 9 PM"
- "is breakfast included?" -> "Breakfast included with Deluxe Room"

[Upload your screenshot here - the one with Aurora Grand Hotel chat]

## How to Run

### Backend

cd backend

pip install -r requirements.txt

python -m uvicorn main:app --reload --port 8000
Backend runs at: http://localhost:8000/docs


### Frontend
cd frontend

npm.cmd install

npm.cmd run dev

Frontend runs at: http://localhost:5173

## Tech Stack
- FastAPI
- Uvicorn
- Pydantic
- React + Vite
