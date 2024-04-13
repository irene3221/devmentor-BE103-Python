from typing import List

from requests import Session

from database.user import User
from notifications.email import EMailNotification
from repository.user import get_user_name_by_id


class EmailService:
    def send(self, db: Session, user_ids: List[int], message: str):
        for user_id in user_ids:
            users: User = get_user_name_by_id(db,user_id)
            EMailNotification().send_notification(users.username, message)