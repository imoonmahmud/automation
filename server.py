from flask import Flask, request
from db import add_order

app = Flask(__name__)

@app.route("/webhook", methods=['POST'])
def webhook():
    data = request.get_json(silent=True)
    required_keys = ['order_id', 'customer_name', 'amount']

    if data is None:
        return {"error:": "no JSON received"}, 400
    elif all(key in data for key in required_keys):
        result = add_order(data['order_id'], data['customer_name'], data['amount'])
        return {'status': result}, 200
    else:
        return {"error": "missing keys"}, 400
    

if __name__ == "__main__":
    app.run(debug=True)