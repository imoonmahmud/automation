import requests

try:
    r = requests.post(
        "http://127.0.0.1:5000/webhook", 
        json={"event": "order_created", "id": 101})
    if r.status_code == 200:
        print("OK:", r.json())
    else:
        print("Failed:", r.status_code, r.text)
except requests.exceptions.ConnectionError:
    print("Server is not reachable")