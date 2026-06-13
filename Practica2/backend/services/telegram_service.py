import os
import requests

from dotenv import load_dotenv

load_dotenv()


class TelegramBot:

    def __init__(self):
        self.token = os.getenv("TOKEN")
        self.chat_id = os.getenv("CHAT_ID")
        self.api_url = os.getenv("API_URL")

        self.base_url = (
            f"https://api.telegram.org/bot{self.token}"
        )

    def change_chat(self, chat_id):
        self.chat_id = chat_id

    def send_message(self, message):

        response = requests.post(
            f"{self.base_url}/sendMessage",
            json={
                "chat_id": self.chat_id,
                "text": message
            }
        )

        return response.json()

    def get_updates(self, offset=None):

        params = {}

        if offset is not None:
            params["offset"] = offset

        response = requests.get(
            f"{self.base_url}/getUpdates",
            params=params
        )

        return response.json()

    def search_question(self, question):

        response = requests.post(
            f"{self.api_url}/questions/search",
            json={
                "question": question
            }
        )

        return response.json()