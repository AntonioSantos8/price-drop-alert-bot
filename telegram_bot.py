import requests

TOKEN = "BOT_TOKEN"
CHAT_ID = "BOTCHAT_ID"

def send_message(text):

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": text
    }

    requests.post(url, data=data)