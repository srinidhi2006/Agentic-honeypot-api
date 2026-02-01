import requests
import time

API_URL = "http://127.0.0.1:8000/analyze"
API_KEY = "MY_SECRET_KEY_4101211"

session_id = "demo-001"

messages = [
    "This is bank support",
    "Your account will be blocked",
    "Send money to UPI",
    "Send to abc@upi"
]

headers = {
    "Content-Type": "application/json",
    "x-api-key": API_KEY
}

for msg in messages:

    payload = {
        "sessionId": session_id,
        "message": {
            "sender": "scammer",
            "text": msg,
            "timestamp": "2026-01-21T10:00:00Z"
        },
        "conversationHistory": [],
        "metadata": {
            "channel": "SMS",
            "language": "English",
            "locale": "IN"
        }
    }

    response = requests.post(API_URL, json=payload, headers=headers)

    print(f"Scammer: {msg}")

    try:
        print("Agent  :", response.json().get("reply"))
    except Exception:
        print("Agent  : ❌ Invalid response")
        print("Raw    :", response.text)

    print("-" * 40)

    time.sleep(1)
