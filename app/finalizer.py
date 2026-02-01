# app/finalizer.py
from app.constants import MAX_TURNS, MIN_RISK_SCORE

def should_finalize(session, detection):
    if session["turns"] >= MAX_TURNS:
        return True

    if detection["scamDetected"] and detection["riskScore"] >= MIN_RISK_SCORE:
        return True

    if "PAYMENT_EXTRACTION" in detection["phaseHistory"]:
        return True

    return False
