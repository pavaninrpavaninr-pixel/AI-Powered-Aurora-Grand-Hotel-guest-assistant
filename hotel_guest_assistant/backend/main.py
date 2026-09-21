from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from datetime import date
from pathlib import Path
import json, logging, re

logging.basicConfig(level=logging.INFO)
app = FastAPI(title='Hotel Guest Assistant API', version='1.0.0')
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_credentials=True, allow_methods=['*'], allow_headers=['*'])

KB = json.loads((Path(__file__).parent.parent / 'data' / 'hotel.json').read_text())

class AvailabilityRequest(BaseModel):
    checkIn: date
    checkOut: date
    adults: int = Field(ge=1, le=10)

class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=1000)
    history: list[dict] = []
    availability: AvailabilityRequest | None = None


def check_availability(req: AvailabilityRequest):
    if req.checkOut <= req.checkIn:
        return {'ok': False, 'error': 'Check-out date must be after check-in date.'}
    nights = (req.checkOut - req.checkIn).days
    results = []
    for room in KB['rooms']:
        if room['capacity'] >= req.adults:
            results.append({**room, 'total': room['pricePerNight'] * nights, 'nights': nights})
    return {'ok': True, 'checkIn': str(req.checkIn), 'checkOut': str(req.checkOut), 'adults': req.adults, 'rooms': results}


def answer(message: str):
    m = message.lower()
    if any(x in m for x in ['check-in', 'check in', 'arrival']): return KB['policies']['checkIn']
    if any(x in m for x in ['check-out', 'check out', 'departure']): return KB['policies']['checkOut']
    if 'pool' in m or 'swimming' in m: return KB['amenities']['pool']
    if 'breakfast' in m: return KB['policies']['breakfast']
    if 'cancel' in m: return KB['policies']['cancellation']
    if 'wifi' in m or 'wi-fi' in m or 'internet' in m: return KB['amenities']['wifi']
    if 'parking' in m: return KB['amenities']['parking']
    if 'three' in m or '3 guest' in m or '3 people' in m: return 'For three guests, the Family Room is suitable because it accommodates up to 4 guests.'
    if any(x in m for x in ['room', 'accommodation', 'stay']):
        return 'We offer ' + ', '.join(r['name'] for r in KB['rooms']) + '. You can ask me about capacity or availability.'
    return "I can help with check-in, check-out, rooms, amenities, breakfast, cancellation policy, Wi-Fi, parking, and room availability. Could you rephrase your question?"

@app.get('/api/health')
def health(): return {'status': 'ok'}

@app.get('/api/hotel')
def hotel(): return KB

@app.post('/api/chat')
def chat(req: ChatRequest):
    logging.info('Chat request received')
    if req.availability:
        return {'type': 'availability', 'message': 'Here are the available room options based on your details.', 'data': check_availability(req.availability)}
    msg = req.message
    wants_availability = any(x in msg.lower() for x in ['available', 'availability', 'vacancy', 'book a room'])
    if wants_availability:
        return {'type': 'need_availability', 'message': 'Please provide your check-in date, check-out date, and number of guests so I can check room availability.'}
    return {'type': 'answer', 'message': answer(msg)}

@app.post('/api/availability')
def availability(req: AvailabilityRequest):
    return check_availability(req)
