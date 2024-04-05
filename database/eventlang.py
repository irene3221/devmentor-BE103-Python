from sqlalchemy import Boolean, Column, Integer, String
from infrastructure.mysql import Base


class EventLang(Base):
    __tablename__ = 'events_langs'

    id = Column(Integer, primary_key=True)
    event_id = Column(Integer)
    lang_id = Column(Integer)
    content = Column(String)

