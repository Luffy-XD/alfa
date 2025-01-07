from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv
import time

load_dotenv()  # Memuat variabel lingkungan dari .env

app = Flask(__name__)

API_URL = "https://api.whatsapp.com/send"  # Ganti dengan URL API WhatsApp yang sesuai
API_TOKEN = os.getenv("API_TOKEN")  # Ambil token dari .env

def send_message(to, body):
    payload = {
        "to": to,
        "body": body
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.post(API_URL, json=payload, headers=headers)
    return response.json()

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if "messages" in data:
        for message in data["messages"]:
            sender = message["from"]
            text = message.get("body", "")
            if text.lower() == "ingatkan polling":
                reminder_message = "Jangan lupa untuk ikut voting di polling kami! Suara Anda sangat berarti!"
                send_message(sender, reminder_message)
    return jsonify({"status": "success"}), 200

def remind_polling(group_id, message, interval):
    while True:
        send_message(group_id, message)
        time.sleep(interval)

if __name__ == '__main__':
    # Ganti dengan ID grup dan pesan pengingat
    group_id = "1234567890@c.us"  # Ganti dengan ID grup WhatsApp Anda
    reminder_message = "Jangan lupa untuk ikut voting di polling kami! Suara Anda sangat berarti!"
    remind_interval = 3600  # Interval dalam detik (misalnya, setiap jam)
    
    # Jalankan pengingat polling di thread terpisah
    from threading import Thread
    reminder_thread = Thread(target=remind_polling, args=(group_id, reminder_message, remind_interval))
    reminder_thread.start()

    app.run(port=5000)
