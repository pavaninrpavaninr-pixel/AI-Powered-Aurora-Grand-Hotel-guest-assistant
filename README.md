<img width="1846" height="920" alt="Screenshot 2026-09-22 002213" src="https://github.com/user-attachments/assets/6d57e251-322f-485e-97d3-b4f9e1517e40" />
<img width="1846" height="920" alt="Screenshot 2026-09-22 002213" src="https://github.com/user-attachments/assets/e33f5ace-ceea-4497-b69e-8675147a850d" />
<img width="1846" height="920" alt="Screenshot 2026-09-22 002213" src="https://github.com/user-attachments/assets/94b02efe-1638-411e-bb5e-26f56d194cb8" />
<img width="1846" height="920" alt="Screenshot 2026-09-22 002213" src="https://github.com/user-attachments/assets/ff8ab384-9fbb-4e5b-b6af-d1cdb2acaf13" />
<img width="1846" height="920" alt="Screenshot 2026-09-22 002213" src="https://github.com/user-attachments/assets/4f76dbe8-8e5a-4d26-99bd-73ea455c7acc" />
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
