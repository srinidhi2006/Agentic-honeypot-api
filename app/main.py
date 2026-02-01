from fastapi import FastAPI, Header, HTTPException
from app.models import IncomingMessage, AgentResponse
from app.auth import verify_api_key
from app.session import get_session
from app.scam_detector import detect_scam_ultra


app = FastAPI(title="Agentic Honeypot API")

@app.post("/analyze", response_model=AgentResponse)
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

    if detection["scamDetected"]:
        reply_text = "I don’t understand this. Can you explain again?"
    else:
        reply_text = "Okay, please continue."

    return AgentResponse(
        status="success",
        reply=reply_text
    )
