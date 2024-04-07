import requests

class LineNotification:
    channel_access_token = None
    def __init__(self, channel_access_token):
        self.channel_access_token = channel_access_token

    @classmethod
    def prepare_notification(cls, user_id, message):
        url = "https://api.line.me/v2/bot/message/push"
        headers = {
            "Authorization": "Bearer " + cls.channel_access_token,
            "Content-Type": "application/json"
        }
        data = {
            "to": user_id,
            "messages": [
                {
                    "type": "text",
                    "text": message
                }
            ]
        }
        return url, headers, data

    @classmethod
    def send_notification(cls, url, headers, data):
        try:
            response = requests.post(url, headers=headers, json=data)
            if response.ok:
                print("Line notification sent successfully")
            else:
                print("Failed to send Line notification:", response.text)
        except Exception as e:
            print("Failed to send Line notification:", str(e))

