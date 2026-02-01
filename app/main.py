from fastapi import FastAPI, Header
from app.models import IncomingMessage
from app.auth import verify_api_key
from app.session import get_session
from app.scam_detector import detect_scam_ultra
from app.agent import generate_agent_reply

app = FastAPI(title="Agentic Honeypot API")


@app.post("/analyze")
def analyze_message(
    payload: IncomingMessage,
    x_api_key: str = Header(None)
):
    verify_api_key(x_api_key)

    session = get_session(payload.sessionId)

    detection = detect_scam_ultra(
        payload.message.text,
        session["behavior"]
    )

    reply_text = generate_agent_reply(
        detection,
        session["agent"],
        payload.message.text
    )

    return {
        "status": "success",
        "reply": reply_text,
        "narrative": detection.get("narrative"),
        "confidence": detection.get("confidence")
    }
