from app.scam_detector import ScamBehaviorState

sessions = {}

def get_session(session_id: str):
    if session_id not in sessions:
        sessions[session_id] = {
            "behavior": ScamBehaviorState(),
            "active": True
        }
    return sessions[session_id]
