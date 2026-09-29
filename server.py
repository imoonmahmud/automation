from flask import Flask, request
from db import add_order
from main import classify_message, extract_lead_info
from sign import verify_signature

app = Flask(__name__)

@app.route("/webhook", methods=['POST'])
def webhook():
    raw_body = request.data
    received_sig = request.headers.get('X-Signature')

    data = request.get_json(silent=True)
    required_keys = ['lead_id', 'message']

    if data is None:
        return {"error:": "no JSON received"}, 400
    elif all(key in data for key in required_keys):
        if verify_signature(raw_body, received_sig):
            category = classify_message(data['message'])
            if category == 'sales':
                info = extract_lead_info(data['message'])
            else:
                info = {'name': None, 'product':None, 'budget': None}
            budget = info.get('budget')
            if budget is not None:
                try:
                    budget = int(budget)
                except (ValueError, TypeError):
                    budget = None

            result = add_order(
                data['lead_id'],
                data['message'],
                category,
                info.get('name'),
                info.get('product'),
                budget
            )
            return {'status': result}, 200
        return {'error': 'missing singature'}
    else:
        return {"error": "missing keys"}, 400


if __name__ == "__main__":
    app.run(debug=True)