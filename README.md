🕵️ Agentic Honeypot API

AI-Driven Scam Detection & Intelligence Extraction

📌 Overview

Agentic Honeypot API is a backend-only AI system that detects scam messages, autonomously engages scammers using a human-like AI agent, extracts scam intelligence, and reports final results to the GUVI evaluation endpoint.

The system is designed as a public REST API, optimized for multi-turn conversations, ethical AI behavior, and structured intelligence reporting.

🎯 Key Capabilities

Detects scam intent from incoming messages

Activates an autonomous honeypot AI agent

Maintains believable human-like conversations

Handles multi-turn chat sessions using sessionId

Extracts actionable scam intelligence:

UPI IDs

Bank accounts

Phishing links

Phone numbers

Suspicious keywords

Sends mandatory final results to GUVI callback endpoint

✨System Architecture (High Level)
Incoming Message (GUVI)
        ↓
API Gateway (FastAPI)
        ↓
Scam Detection Engine
        ↓
Agentic Honeypot Engine
        ↓
Conversation Manager
        ↓
Intelligence Extractor
        ↓
Final Result Callback (GUVI)

🛠️ Tech Stack
Component	Technology
Backend Framework	FastAPI
API Server	Uvicorn
HTTP Client	Requests
Language	Python 3.9+
Storage	In-memory (session-based)
Authentication	API Key (x-api-key)

🔐 API Authentication

All requests must include the API key header:

x-api-key: YOUR_SECRET_API_KEY
Content-Type: application/json


Unauthorized requests will be rejected.

📥 API Input Format
First Message (New Session)
{
  "sessionId": "abc123-session-id",
  "message": {
    "sender": "scammer",
    "text": "Your bank account will be blocked today. Verify immediately.",
    "timestamp": "2026-01-21T10:15:30Z"
  },
  "conversationHistory": [],
  "metadata": {
    "channel": "SMS",
    "language": "English",
    "locale": "IN"
  }
}

Follow-Up Message (Same Session)
{
  "sessionId": "abc123-session-id",
  "message": {
    "sender": "scammer",
    "text": "Share your UPI ID to avoid suspension.",
    "timestamp": "2026-01-21T10:17:10Z"
  },
  "conversationHistory": [
    {
      "sender": "scammer",
      "text": "Your bank account will be blocked today. Verify immediately.",
      "timestamp": "2026-01-21T10:15:30Z"
    },
    {
      "sender": "user",
      "text": "Why will my account be blocked?",
      "timestamp": "2026-01-21T10:16:10Z"
    }
  ]
}



📤 API Output Format (Agent Reply)
{
  "status": "success",
  "reply": "Why is my account being suspended?"
}


⚠️ The reply must appear human-written and must not reveal scam detection.

🧩 Intelligence Extraction

The system extracts and accumulates:

Bank account numbers

UPI IDs

Phishing URLs

Phone numbers

Suspicious keywords (urgent, verify, blocked, etc.)

Extraction occurs only from scammer messages.

🚨 Mandatory Final Callback (CRITICAL)

Once:

Scam intent is confirmed

Agent engagement is completed

Intelligence extraction is finished

The system must send the final result to:

POST https://hackathon.guvi.in/api/updateHoneyPotFinalResult

Callback Payload
{
  "sessionId": "abc123-session-id",
  "scamDetected": true,
  "totalMessagesExchanged": 18,
  "extractedIntelligence": {
    "bankAccounts": ["XXXX-XXXX-XXXX"],
    "upiIds": ["scammer@upi"],
    "phishingLinks": ["http://malicious-link.example"],
    "phoneNumbers": ["+91XXXXXXXXXX"],
    "suspiciousKeywords": ["urgent", "verify now", "account blocked"]
  },
  "agentNotes": "Scammer used urgency and payment redirection tactics"
}


🚨 If this callback is not sent, the solution will NOT be evaluated.

⚖️ Ethical & Safety Compliance

❌ No impersonation of real individuals

❌ No harassment or illegal instructions

✅ Simulated environment only

✅ Responsible handling of extracted data

🚀 How to Run Locally
pip install fastapi uvicorn requests
uvicorn main:app --reload


API will be available at:

http://localhost:8000





