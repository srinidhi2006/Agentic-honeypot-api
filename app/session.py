from app.scam_detector import ScamBehaviorState
from app.agent import AgentState
from app.intelligence import Intelligence

sessions = {}

def get_session(session_id):
    if session_id not in sessions:
        sessions[session_id] = {
            "behavior": ScamBehaviorState(),
            "agent": AgentState(),
            "intelligence": Intelligence(),
            "turns": 0,
            "active": True
        }
    return sessions[session_id]
