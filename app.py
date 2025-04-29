from flask import Flask, request, jsonify

app = Flask(__name__)

VERIFY_TOKEN = 'your_custom_verify_token'

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        # Webhook verification
        mode = request.args.get('hub.mode')
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')

        if mode == 'subscribe' and token == VERIFY_TOKEN:
            print("Webhook verified!")
            return challenge, 200
        else:
            return "Verification failed", 403

    elif request.method == 'POST':
        # Handle incoming messages/events
        data = request.get_json()
        print("Received webhook data:", data)

        # You can process the message or store it here
        return jsonify(success=True), 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)
