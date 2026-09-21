# Evaluation - 10 Scenarios

1. Normal: "What is check-in time?" -> Returns "3 PM" from JSON - PASS
2. Normal: "Do you have swimming pool?" -> Yes with timings - PASS
3. Missing Info: "I need a room" -> Asks checkIn, checkOut, adults - PASS
4. Ambiguous: "Something to eat" -> Shows restaurant, breakfast info - PASS
5. Availability: "Room for 2 on 2026-12-01?" -> Calls checkAvailability tool -> Shows results - PASS
6. Incorrect assumption: "Is breakfast free for 10 people?" -> Corrects based on policy - PASS
7. Follow-up: Q1 "Pool time?" Q2 "And breakfast?" -> Maintains context - PASS
8. Frontend loading: Shows typing dots while backend responds - PASS
9. Backend failure: If LLM fails, returns fallback "Sorry, I could not find..." - PASS
10. E2E: Open app -> Ask question -> See backend call -> Get AI response -> Ask follow-up -> Check availability - PASS
