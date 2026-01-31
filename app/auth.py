from fastapi import HTTPException

API_KEY = "MY_SECRET_KEY_4101211"

def verify_api_key(key: str):
    if key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
