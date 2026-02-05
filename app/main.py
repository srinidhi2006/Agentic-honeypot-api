from fastapi import FastAPI, Header
from app.models import IncomingMessage
from app.auth import verify_api_key
from app.session import get_session
from app.scam_detector import detect_scam_ultra
from app.agent import generate_agent_reply
from fastapi import Depends

from app.intelligence import Intelligence
from app.finalizer import should_finalize
from app.callback import send_final_result
from app.metrics import generate_agent_notes

app = FastAPI(title="Agentic Honeypot API")


@app.post("/analyze")

def analyze_message(payload: IncomingMessage, _: None = Depends(verify_api_key)):

    session = get_session(payload.sessionId)
    session["turns"] += 1

    detection = detect_scam_ultra(
        payload.message.text,
        session["behavior"]
    )

    reply_text = generate_agent_reply(
        detection,
        session["agent"],
        payload.message.text
    )

    session["intelligence"].process_message(
        payload.message.text
    )


    if should_finalize(session, detection):
        send_final_result(
            session_id=payload.sessionId,
            scam_detected=detection["scamDetected"],
            total_messages=session["turns"],
            intelligence=session["intelligence"].export(),
            agent_notes=generate_agent_notes(detection)
        )
        session["active"] = False

    return {
        "status": "success",
        "reply": reply_text,
    }
@app.get("/health")
def health():
    return {"status": "alive"}


