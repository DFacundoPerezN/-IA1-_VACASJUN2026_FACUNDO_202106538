import os
import requests

TOKEN = os.getenv("TOKEN")

def send_message(chat_id, message, token= TOKEN):

    url = f"https://api.telegram.org/bot{token}/sendMessage"

    payload = {
        "chat_id": chat_id,
        "text": message
    }

    response = requests.post(
        url,
        json=payload
    )

    return response.json()