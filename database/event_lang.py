from sqlalchemy import Column, Integer
from infrastructure.mysql import Base

class EventLanguageMapping(Base):
    __tablename__ = "event_language_mapping"

    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, index=True)
    language_id = Column(Integer, index=True)