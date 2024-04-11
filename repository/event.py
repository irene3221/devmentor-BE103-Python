from sqlalchemy.orm import Session
from database.event import Event
from database.eventlang import EventLang
from schema.database.event import EventCreate, EventUpdate, EventBase


def lists(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Event).offset(skip).limit(limit).all()


def create(db: Session, event: EventBase):
    db_user = Event(user_id=event.user_id, name=event.name, date=event.date)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_event(db: Session, event_id: int):
    return db.query(Event).filter(Event.id == event_id).first()


def delete(db: Session, event: Event):
    db.delete(event)
    db.commit()


def patch_event(db: Session, event_id: int, event_update: EventUpdate):
    db_event = get_event(db, event_id)
    if db_event:
        for field, value in event_update.dict(exclude_unset=True).items():
            setattr(db_event, field, value)
        db.commit()
        db.refresh(db_event)
        return db_event
    return None


def get_content(db: Session, event_id: int, lang_id: int):
    result = db.query(EventLang.content).filter(EventLang.event_id == event_id, EventLang.lang_id == lang_id).first()
    if result:
            return result[0]
    return None