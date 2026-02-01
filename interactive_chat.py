import requests
import datetime

API_URL = "http://127.0.0.1:8000/analyze"
API_KEY = "MY_SECRET_KEY_4101211"

session_id = "interactive-session-001"

headers = {
    "Content-Type": "application/json",
    "x-api-key": API_KEY
}

print("\n🟢 Interactive Scam Honeypot Chat")
print("Type scammer messages. Type 'exit' to stop.\n")

while True:
    scammer_text = input("Scammer: ")

    if scammer_text.lower() == "exit":
        print("\n🛑 Chat stopped")
        break

    payload = {
        "sessionId": session_id,
        "message": {
            "sender": "scammer",
            "text": scammer_text,
            "timestamp": datetime.datetime.utcnow().isoformat() + "Z"
        },
        "conversationHistory": [],
        "metadata": {
            "channel": "SMS",
            "language": "English",
            "locale": "IN"
        }
    }

    response = requests.post(API_URL, json=payload, headers=headers)

    if response.status_code != 200:
        print("❌ Server Error:", response.status_code)
        print(response.text)
        continue

    data = response.json()

    # 🧠 Optional debug signals
    narrative = data.get("narrative", "unknown")
    confidence = data.get("confidence", "N/A")

    print(f"🧠 Narrative : {narrative}")
    print(f"📊 Confidence: {confidence}")
    print(f"Agent       : {data.get('reply')}")
    print("-" * 45)
