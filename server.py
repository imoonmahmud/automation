from flask import Flask, request

app = Flask(__name__)

@app.route("/webhook", methods=['POST'])
def webhook():
    data = request.get_json(silent=True)
    if data is None:
        return {"error:": "no JSON received"}, 400
    if 'event' not in data:
        return {"error": "missing event"}, 400
    print("Received:", data)
    return {"status": 'received'}, 200

@app.route("/health", methods=['GET'])
def health():
    return {'ok': True}, 200

if __name__ == "__main__":
    app.run(debug=True)