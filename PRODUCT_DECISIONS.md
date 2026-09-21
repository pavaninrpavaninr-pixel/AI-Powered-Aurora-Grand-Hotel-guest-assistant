# Product, UX, Engineering, AI Decisions

- Customer problem: Guests need 24/7 answers without calling reception.
- Guest journey: Land on site -> Chat icon -> Ask question -> Get instant answer -> Check availability -> Book.
- Why this frontend: Simple chat like WhatsApp, mobile responsive, shows loading/error gracefully.
- AI vs Deterministic: AI for understanding natural language, deterministic for availability check and policies to avoid hallucinations.
- What can go wrong: AI hallucinates room prices. Prevention: Only answer from JSON, fallback if not found.
- Failure handling: Frontend shows "Something went wrong, try again" if backend down.
- How to measure usefulness: Count questions answered without staff, booking conversion.
- Production improvement: Add real DB, auth, analytics, rate limiting.
