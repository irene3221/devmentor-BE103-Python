from sqlalchemy import Column, Integer, String

from infrastructure.mysql import Base


class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    name = Column(String, unique=True)
    date = Column(String)


