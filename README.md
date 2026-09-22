<img width="1846" height="920" alt="Screenshot 2026-09-22 002213" src="https://github.com/user-attachments/assets/4f76dbe8-8e5a-4d26-99bd-73ea455c7acc" />
<img width="1847" height="912" alt="Screenshot 2026-09-22 002234" src="https://github.com/user-attachments/assets/9a1c0c2b-880e-4f81-8403-54bb2d647ae8" />

# Aurora Grand Hotel - Guest Assistant

AI-powered hotel chatbot using FastAPI + React + RAG

## 🚀 Live Demo Proof
Backend and Frontend both working perfectly!

### Chatbot answering:
- "what time is check-in?" -> "Check-in starts at 2:00 PM"
- "Do you have a swimming pool?" -> "outdoor pool open 6 AM to 9 PM"
- "is breakfast included?" -> "Breakfast included with Deluxe Room"

  ### 🔴 Live Demo
Frontend (Vercel): https://ai-powered-aurora-grand-hotel-guest.vercel.app
Backend (Render): https://ai-powered-aurora-grand-hotel-guest.onrender.com
Backend Docs: https://ai-powered-aurora-grand-hotel-guest.onrender.com/docs



## How to Run

### Backend
```bash
cd backend
pip install -r requirements.txt
python -m uvicorn main:app --reload --port 8000
```
Backend runs at: http://localhost:8000/docs


### Frontend
```bash
cd frontend
npm.cmd install
npm.cmd run dev
```
Frontend runs at: http://localhost:5173

## Tech Stack
- FastAPI
- Uvicorn
- Pydantic
- React + Vite
