import requests


def send_request(payload):
    try:
        response = requests.post("http://127.0.0.1:5000/webhook", json=payload)
        if response.status_code == 200:
            print('OK:', response.json())
        else:
            print('Failed:', response.status_code, response.text)
            
    except requests.exceptions.ConnectionError:
        print("Server is not reachable")

send_request({"lead_id": "L002", "message": "I am looking for an iPhone 15. My name is Karim and I can spend around $700."})