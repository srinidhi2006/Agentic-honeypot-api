# app/intelligence.py
import re

UPI_REGEX = r"[a-zA-Z0-9.\-_]{2,}@[a-zA-Z]{2,}"
PHONE_REGEX = r"\+91[0-9]{10}|[0-9]{10}"
URL_REGEX = r"https?://[^\s]+"

class Intelligence:
    def __init__(self):
        self.upiIds = set()
        self.phoneNumbers = set()
        self.phishingLinks = set()
        self.bankAccounts = set()
        self.suspiciousKeywords = set()

    def process_message(self, text: str):
        text_lower = text.lower()

        self.upiIds.update(re.findall(UPI_REGEX, text))
        self.phoneNumbers.update(re.findall(PHONE_REGEX, text))
        self.phishingLinks.update(re.findall(URL_REGEX, text))

        for word in text_lower.split():
            if word in ["otp", "pin", "password"]:
                self.suspiciousKeywords.add(word)

    def export(self):
        return {
            "bankAccounts": list(self.bankAccounts),
            "upiIds": list(self.upiIds),
            "phishingLinks": list(self.phishingLinks),
            "phoneNumbers": list(self.phoneNumbers),
            "suspiciousKeywords": list(self.suspiciousKeywords)
        }
