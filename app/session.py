sessions = {}

def get_session(session_id: str):
    if session_id not in sessions:
        sessions[session_id] = {
            "messages": [],
            "active": True
        }
    return sessions[session_id]
