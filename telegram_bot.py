import requests


BOT_TOKEN = "8529187564:AAGSBqxzHAXSe0iQ428yvvo34urMMwGQV5g"
CHAT_ID = "557655586"


def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": text
    }

    response = requests.post(url, data=data)

    return response.json()