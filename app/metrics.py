# app/metrics.py

def generate_agent_notes(detection):
    notes = []

    if "URGENCY_PRESSURE" in detection["phaseHistory"]:
        notes.append("Used urgency tactics")

    if "AUTHORITY_ASSERTION" in detection["phaseHistory"]:
        notes.append("Impersonated authority")

    if "PAYMENT_EXTRACTION" in detection["phaseHistory"]:
        notes.append("Attempted monetary extraction")

    return ", ".join(notes)
