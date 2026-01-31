from fastapi import FastAPI, Header, HTTPException
from app.models import IncomingMessage, AgentResponse
from app.auth import verify_api_key
from app.session import get_session

app = FastAPI(title="Agentic Honeypot API")

@app.post("/analyze", response_model=AgentResponse)
def analyze_message(
    payload: IncomingMessage,
    x_api_key: str = Header(None)
):
    verify_api_key(x_api_key)

    session = get_session(payload.sessionId)

    # Temporary placeholder reply
    reply_text = "Why will my account be blocked?"

    return AgentResponse(
        status="success",
        reply=reply_text
    )
