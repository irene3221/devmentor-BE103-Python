from typing import List
from notifications.telegram import TelegramNotification


class NotificationService:
    def __init__(self, telegram_bot_token: str = None):
        self.telegram_notifier = TelegramNotification(bot_token=telegram_bot_token)

    def send_telegram_notification(self, chat_ids: List[int], message: str):
        for chat_id in chat_ids:
            self.telegram_notifier.send_notification(chat_id, message)