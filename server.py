from flask import Flask, request
from db import add_order
from main import classify_message, extract_lead_info

app = Flask(__name__)

@app.route("/webhook", methods=['POST'])
def webhook():
    data = request.get_json(silent=True)
    required_keys = ['lead_id', 'message']

    if data is None:
        return {"error:": "no JSON received"}, 400
    elif all(key in data for key in required_keys):
        category = classify_message(data['message'])
        lead_info = extract_lead_info(data['message'])
        budget = lead_info.get('budget')
        if budget is not None:
            try:
                budget = int(budget)
            except (ValueError, TypeError):
                budget = None

        result = add_order(
            data['lead_id'],
            data['message'],
            category,
            lead_info.get('name'),
            lead_info.get('product'),
            budget
        )
        return {'status': result}, 200
    else:
        return {"error": "missing keys"}, 400
    

if __name__ == "__main__":
    app.run(debug=True)