class TelegramNotification:
    def __init__(self, bot_token):
        self.bot_token = bot_token

    def send_notification(self, user_name: str, message: str):
        print("telegram sent, user name: {}, message: {}".format(user_name,message))
