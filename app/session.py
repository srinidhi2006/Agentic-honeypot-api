from app.scam_detector import ScamBehaviorState
from app.agent import AgentState

sessions = {}

def get_session(session_id: str):
    if session_id not in sessions:
        sessions[session_id] = {
            "behavior": ScamBehaviorState(),
            "agent": AgentState(),
            "active": True
        }
    return sessions[session_id]
