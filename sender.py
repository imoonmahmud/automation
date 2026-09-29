import requests
import json
from sign import sign_payload

def send_request(payload):
    body, sig = sign_payload(payload)
    try:
        response = requests.post(
            "http://127.0.0.1:5000/webhook", 
            data=body,
            headers={"Content-Type": "application/json", "X-Signature": sig}
        )
        if response.status_code == 200:
            print('OK:', response.json())
        else:
            print('Failed:', response.status_code, response.text)
            
    except requests.exceptions.ConnectionError:
        print("Server is not reachable")

send_request({"lead_id": "L012", "message": "Do you deliver to Dhaka?"})