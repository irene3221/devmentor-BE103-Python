from sqlalchemy.orm import Session
from database.userevent import UserEvent


def get_user_subscribe(db: Session, event_id: int):
    return db.query(UserEvent.user_id).filter(UserEvent.event_id == event_id).all()

