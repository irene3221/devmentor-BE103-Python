from typing import List

from requests import Session

from database.user import User
from notifications.line import LineNotification
from repository.user import get_user_name_by_id


class LineService:
    def send(self, db: Session, user_ids: List[int], message: str):
        for user_id in user_ids:
            users: User = get_user_name_by_id(db,user_id)
            LineNotification().send_notification(users.username, message)