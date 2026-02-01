# app/agent.py
import random


class AgentState:
    def __init__(self):
        self.turn_count = 0
        self.persona = None
        self.last_reply = None


def detect_persona(text: str):
    text = text.lower()

    if any(x in text for x in ["son", "grandson", "retired", "pension"]):
        return "elderly"

    if any(x in text for x in ["office", "meeting", "salary", "work"]):
        return "professional"

    if any(x in text for x in ["bro", "lol", "insta", "game"]):
        return "teenager"

    return "elderly"


# 🔥 Narrative + Persona based replies
NARRATIVE_PERSONA_REPLIES = {
    "reward": {
        "elderly": {
            "confused": [
                "I never applied for any prize.",
                "Why am I getting this message?",
                "I don’t remember entering any contest.",
                "Is this really meant for me?",
                "Who sent this message?",
            ],
            "probe": [
                "How did I win this?",
                "What do I need to do to get it?",
                "Is there any verification?",
                "Where can I confirm this?",
                "Is there a deadline?",
            ],
        },
        "professional": {
            "confused": [
                "I don’t recall participating in this.",
                "Which lottery is this?",
                "I haven’t received any official email.",
                "What organization is conducting this?",
                "This is unexpected.",
            ],
            "probe": [
                "Please share the verification process.",
                "How was the winner selected?",
                "Is there an official website?",
                "Who is the issuing authority?",
                "Can this be independently verified?",
            ],
        },
        "teenager": {
            "confused": [
                "Bro I didn’t enter anything.",
                "What jackpot?",
                "This sounds fake.",
                "Why did I get this message?",
                "Is this some prank?",
            ],
            "probe": [
                "How did I win?",
                "What do I need to do?",
                "Is there a link?",
                "How much did I win?",
                "Is this real?",
            ],
        },
    },

    "threat": {
        "elderly": {
            "confused": [
                "Why will my account be blocked?",
                "I didn’t do anything wrong.",
                "I am scared reading this.",
                "Is my money safe?",
                "Why is this happening to me?",
            ],
            "probe": [
                "What should I do now?",
                "Which account is this?",
                "Can my son help with this?",
                "Is this very urgent?",
                "How serious is this?",
            ],
        },
        "professional": {
            "confused": [
                "I haven’t received any official notice.",
                "Can you clarify the issue?",
                "Which regulation is this related to?",
                "I don’t see any alerts on my account.",
                "This is concerning.",
            ],
            "probe": [
                "What is the escalation process?",
                "How can I verify this?",
                "Which account is affected?",
                "Is there a reference number?",
                "What is the deadline?",
            ],
        },
        "teenager": {
            "confused": [
                "Why is my account blocked?",
                "This doesn’t make sense.",
                "I didn’t even do anything.",
                "This sounds weird.",
                "Who sent this?",
            ],
            "probe": [
                "What do I need to do?",
                "Which account?",
                "Is there a link?",
                "How can I fix this?",
                "Is this urgent?",
            ],
        },
    },

    "authority": {
        "elderly": {
            "confused": [
                "Are you from the bank?",
                "Why are you calling me?",
                "Which bank is this?",
                "How did you get my number?",
                "Is this official?",
            ],
            "probe": [
                "Can you explain slowly?",
                "Can I visit the branch?",
                "Who should I talk to?",
                "Is there a letter?",
                "How can I confirm this?",
            ],
        },
        "professional": {
            "confused": [
                "Which department are you calling from?",
                "Is this an official call?",
                "Why is this not via email?",
                "I need verification.",
                "This seems unusual.",
            ],
            "probe": [
                "Please share your employee ID.",
                "How can I verify this?",
                "Is there an official reference?",
                "Can you send documentation?",
                "What is the next step?",
            ],
        },
        "teenager": {
            "confused": [
                "Who are you?",
                "Why are you messaging me?",
                "This feels fake.",
                "I don’t trust this.",
                "Why should I reply?",
            ],
            "probe": [
                "Send proof.",
                "How do I verify?",
                "Is there a link?",
                "Where can I check?",
                "Is this legit?",
            ],
        },
    },

    "unknown": {
        "elderly": {
            "confused": [
                "I don’t understand this.",
                "Why are you asking me this?",
                "I am confused.",
                "This message is unclear.",
                "Can you explain slowly?",
            ],
            "probe": [
                "What exactly do you want?",
                "Why do you need this?",
                "Is this important?",
                "Who are you?",
                "What should I do?",
            ],
        },
        "professional": {
            "confused": [
                "This request is unclear.",
                "Please clarify your message.",
                "I need more information.",
                "This seems vague.",
                "Why was I contacted?",
            ],
            "probe": [
                "Can you provide more details?",
                "What is the purpose of this?",
                "Is there documentation?",
                "How can I verify this?",
                "What action is required?",
            ],
        },
        "teenager": {
            "confused": [
                "What is this about?",
                "Why are you asking me?",
                "This sounds weird.",
                "I don’t get it.",
                "Explain properly.",
            ],
            "probe": [
                "What do you want?",
                "Why me?",
                "Is there a link?",
                "How do I check?",
                "What happens next?",
            ],
        },
    },
}


def generate_agent_reply(detection, agent_state: AgentState, message_text: str):

    agent_state.turn_count += 1

    if agent_state.persona is None:
        agent_state.persona = detect_persona(message_text)

    persona = agent_state.persona
    narrative = detection.get("narrative", "unknown")

    replies = NARRATIVE_PERSONA_REPLIES.get(
        narrative,
        NARRATIVE_PERSONA_REPLIES["unknown"]
    )[persona]

    if agent_state.turn_count <= 2:
        pool = replies["confused"]
    else:
        pool = replies["probe"]

    choice = random.choice(pool)
    while choice == agent_state.last_reply and len(pool) > 1:
        choice = random.choice(pool)

    agent_state.last_reply = choice
    return choice
