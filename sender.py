import requests

try:
    response = requests.post(
        "http://127.0.0.1:5000/webhook",
        json={
            'order_id': 125,
            'customer_name': 'Emon Mahmud',
            'amount': 356})
    
    if response.status_code == 200:
        print('OK:', response.json())
    else:
        print('Failed:', response.status_code, response.text)
        
except requests.exceptions.ConnectionError:
    print("Server is not reachable")
