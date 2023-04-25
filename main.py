from flask import Flask, request, jsonify

from telethon import TelegramClient, events, sync

import os

app = Flask(__name__)

# Telegram API credentials

api_id = os.environ.get('API_ID')

api_hash = os.environ.get('API_HASH')

# Initialize Telegram client

client = TelegramClient('session', api_id, api_hash)

@app.route('/send_code', methods=['POST'])

def send_code():

    phone = request.json['phone']

    try:

        client.send_code_request(phone)

        return jsonify({'message': 'Verification code sent successfully.'}), 200

    except Exception as e:

        return jsonify({'error': str(e)}), 400

@app.route('/submit_code', methods=['POST'])

def submit_code():

    code = request.json['code']

    try:

        client.sign_in(code=code)

        return jsonify({'message': 'Verification successful.'}), 200

    except Exception as e:

        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':

    app.run(debug=True)

