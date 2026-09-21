from fastapi.testclient import TestClient
from main import app
client = TestClient(app)

def test_health(): assert client.get('/api/health').json()['status'] == 'ok'
def test_faq(): assert '2:00 PM' in client.post('/api/chat', json={'message':'What time is check-in?'}).json()['message']
def test_unknown(): assert client.post('/api/chat', json={'message':'Do you have a gym?'}).json()['type'] == 'answer'
def test_invalid_dates():
    r=client.post('/api/availability',json={'checkIn':'2026-10-10','checkOut':'2026-10-09','adults':2}).json(); assert r['ok'] is False
def test_availability():
    r=client.post('/api/availability',json={'checkIn':'2026-10-10','checkOut':'2026-10-12','adults':3}).json(); assert len(r['rooms']) == 2
