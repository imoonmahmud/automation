import json
from server import app
from sign import sign_payload

def test_webhook_valid_save_lead():
    app.testing = True
    client = app.test_client()

    body, sig = sign_payload({"lead_id": "TEST001", "message": "Do you deliver to Dhaka?"})

    response = client.post(
        "/webhook",
        data=body,
        headers={"Content-Type": "application/json", "X-Signature": sig}
    )

    assert response.status_code == 200