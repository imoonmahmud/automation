from sign import sign_payload, verify_signature

def test_valid_signature_passes():
    body, sig = sign_payload({"lead_id": "L1", "message": "hi"})
    assert verify_signature(body, sig) == True

def test_tampered_signature_fails():
    body, sig = sign_payload({"lead_id": "L1", "message": "hi"})
    tampered_body = body.replace(b"hi", b"bye")
    assert verify_signature(tampered_body, sig) == False

def test_wrong_signature_fails():
    body, sig = sign_payload({"lead_id": "L012", "message": "Do you deliver to Dhaka?"})
    assert verify_signature(body, '02445+9dasf') == False




