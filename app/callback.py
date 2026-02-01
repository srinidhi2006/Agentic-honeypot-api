# app/callback.py
import requests

GUVI_ENDPOINT = "https://hackathon.guvi.in/api/updateHoneyPotFinalResult"

def send_final_result(
    session_id,
    scam_detected,
    total_messages,
    intelligence,
    agent_notes
):
    payload = {
        "sessionId": session_id,
        "scamDetected": scam_detected,
        "totalMessagesExchanged": total_messages,
        "extractedIntelligence": intelligence,
        "agentNotes": agent_notes
    }

    print(payload)

    try:
        response = requests.post(
            "https://hackathon.guvi.in/api/updateHoneyPotFinalResult",
            json=payload,
            timeout=5
        )
        print("✅ GUVI CALLBACK STATUS:", response.status_code)
    except Exception as e:
        print("❌ GUVI CALLBACK FAILED:", e)
