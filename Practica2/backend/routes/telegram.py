from flask import Blueprint, jsonify

from services.telegram_service import TelegramBot

telegram_bp = Blueprint(
    "telegram",
    __name__,
    url_prefix="/telegram"
)

bot = TelegramBot()

offset = None

@telegram_bp.route("/check", methods=["GET"])
def check_messages():

    updates = bot.get_updates()

    return jsonify(updates)

@telegram_bp.route("/process", methods=["GET"])
def process_messages():

    global offset

    updates = bot.get_updates(offset)

    for update in updates["result"]:

        offset = update["update_id"] + 1

        message = update.get("message")

        if not message:
            continue

        text = message.get("text", "")

        chat_id = message["chat"]["id"]

        bot.change_chat(chat_id)

        result = bot.search_question(text)

        bot.send_message(
            result["answer"]
        )

    return jsonify({
        "message": "Procesado"
    })