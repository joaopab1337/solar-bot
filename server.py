from flask import Flask, request, jsonify
from solar_bot import *
from config import TELEGRAM_SET_WEBHOOK_URL

server = Flask(__name__)
init_webhook(TELEGRAM_SET_WEBHOOK_URL)

@server.route('/webhook', methods=['POST'])
def index():
    webhook_data = request.get_json()
    print(webhook_data)
    action = webhook_data['message']['text'].lower()
    success = handle_action(webhook_data, action)
    return jsonify(success=success)

if __name__ == '__main__':
    server.run(port=5000)
