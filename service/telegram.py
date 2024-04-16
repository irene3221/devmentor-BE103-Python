from typing import List

from requests import Session

from database.user import User
from notifications.telegram import TelegramNotification
from repository.user import get_user_name_by_id


class TelegramService:
    def __init__(self, telegram_bot_token: str = None):
        self.telegram_notifier = TelegramNotification(bot_token=telegram_bot_token)

    def send(self, db: Session, user_ids: List[int], message: str):
        for user_id in user_ids:
            users: User = get_user_name_by_id(db, user_id)
            self.telegram_notifier.send_notification(users.username, message)