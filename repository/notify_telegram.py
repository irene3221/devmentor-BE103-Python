import requests

class TelegramNotification:
    def __init__(self, bot_token):
        self.bot_token = bot_token

    def send_notification(self, chat_id, message):
        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
        params = {
            "chat_id": chat_id,
            "text": message
        }
        try:
            response = requests.post(url, json=params)
            if response.ok:
                print("Telegram notification sent successfully")
            else:
                print("Failed to send Telegram notification:", response.text)
        except Exception as e:
            print("Failed to send Telegram notification:", str(e))

