import hmac
import hashlib
import json
import os
from dotenv import load_dotenv

SECRET = os.getenv('WEBHOOK_SECRET')

def sign_payload(payload_dict):
    payload_bytes = json.dumps(payload_dict).encode()
    signature = hmac.new(SECRET.encode(), payload_bytes, hashlib.sha256).hexdigest()
    return payload_bytes, signature

payload = {"lead_id": "L010", "message": "test"}

def verify_signature(raw_body, received_signature):
    expected = hmac.new(SECRET.encode(), raw_body, hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected, received_signature)
