import time

from services.telegram_service import TelegramBot

bot = TelegramBot()

offset = None


def start_listener():

    global offset

    print("Telegram listener iniciado")

    while True:

        try:

            updates = bot.get_updates(offset)

            for update in updates["result"]:

                offset = update["update_id"] + 1

                message = update.get("message")

                if not message:
                    continue

                text = message.get(
                    "text",
                    ""
                )

                chat_id = message["chat"]["id"]

                bot.change_chat(chat_id)

                result = bot.search_question(
                    text
                )

                answer = result.get(
                    "answer",
                    "No encontré una respuesta."
                )

                bot.send_message(
                    answer
                )

            time.sleep(0.5)

            print("Telegram listener escuchando")

        except Exception as e:

            print(
                f"Error Telegram: {e}"
            )

            time.sleep(5)