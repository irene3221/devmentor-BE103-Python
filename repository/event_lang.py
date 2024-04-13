from sqlalchemy.orm import Session

from database.eventlang import EventLang


def create(db: Session, event_lang: EventLang):
    db.add(event_lang)
    db.commit()
    db.refresh(event_lang)
    return event_lang
