from sqlalchemy import select
from sqlalchemy.orm import Session
from database.event_lang import EventLanguageMapping

def get_event_language_mapping_by_ids(db: Session, event_id: int, language_id: int):
    query = select(EventLanguageMapping).where(
        EventLanguageMapping.event_id == event_id,
        EventLanguageMapping.language_id == language_id
    )
    result = db.execute(query)
    return result.first()
