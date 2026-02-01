class ScamBehaviorState:
    """
    Tracks adversarial scammer behavior across a session.
    """

    def __init__(self):
        self.current_phase = "INITIAL_CONTACT"
        self.phase_history = []
        self.risk_score = 0
        self.behavioral_signals = set()

    def advance(self, phase: str, points: int, signal: str):
        self.current_phase = phase
        self.phase_history.append(phase)
        self.risk_score += points
        self.behavioral_signals.add(signal)
SCAM_PHASES = [
    "INITIAL_CONTACT",
    "URGENCY_PRESSURE",
    "AUTHORITY_ASSERTION",
    "ACTION_REQUEST",
    "ISOLATION_TACTIC",
    "PAYMENT_EXTRACTION"
]
INTENT_SIGNALS = {
    "THREAT": ["blocked", "suspended", "legal action", "freeze"],
    "REWARD": ["prize", "won", "cashback"],
    "AUTHORITY": ["bank", "upi", "customer care", "support", "govt"],
    "ACTION": ["click", "verify", "share", "send"],
    "SENSITIVE": ["otp", "pin", "password", "upi id"],
    "ISOLATION": ["do not tell", "confidential", "keep secret"],
    "PAYMENT": ["pay", "transfer", "send money", "upi"]
}
def resolve_behavior_phase(text: str, behavior: ScamBehaviorState):
    text = text.lower()

    if any(x in text for x in INTENT_SIGNALS["THREAT"]):
        behavior.advance("URGENCY_PRESSURE", 2, "Threat pressure")

    if any(x in text for x in INTENT_SIGNALS["AUTHORITY"]):
        behavior.advance("AUTHORITY_ASSERTION", 3, "Authority impersonation")

    if any(x in text for x in INTENT_SIGNALS["ACTION"]):
        behavior.advance("ACTION_REQUEST", 3, "Action enforcement")

    if any(x in text for x in INTENT_SIGNALS["ISOLATION"]):
        behavior.advance("ISOLATION_TACTIC", 2, "Isolation manipulation")

    if any(x in text for x in INTENT_SIGNALS["PAYMENT"]):
        behavior.advance("PAYMENT_EXTRACTION", 5, "Monetization attempt")

    if any(x in text for x in INTENT_SIGNALS["SENSITIVE"]):
        behavior.advance("PAYMENT_EXTRACTION", 5, "Sensitive data theft")
def follows_scam_trajectory(behavior: ScamBehaviorState):
    required_sequence = [
        "URGENCY_PRESSURE",
        "AUTHORITY_ASSERTION",
        "ACTION_REQUEST",
        "PAYMENT_EXTRACTION"
    ]

    return all(phase in behavior.phase_history for phase in required_sequence)

def detect_scam_ultra(message: str, behavior: ScamBehaviorState):
    resolve_behavior_phase(message, behavior)

    # Base detection logic
    scam_detected = (
        behavior.risk_score >= 8 or
        follows_scam_trajectory(behavior)
    )

    # 🔥 NEW: Combined psychological manipulation trigger
    isolation_present = "ISOLATION_TACTIC" in behavior.phase_history
    manipulation_present = any(
        phase in behavior.phase_history
        for phase in ["URGENCY_PRESSURE", "AUTHORITY_ASSERTION", "ACTION_REQUEST"]
    )

    if isolation_present and manipulation_present:
        scam_detected = True

    return {
        "scamDetected": scam_detected,
        "riskScore": behavior.risk_score,
        "currentPhase": behavior.current_phase,
        "phaseHistory": behavior.phase_history,
        "confidence": min(behavior.risk_score / 12, 0.98),
        "behavioralSignals": list(behavior.behavioral_signals)
    }
