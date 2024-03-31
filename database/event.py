from sqlalchemy import Boolean, Column, Integer, String

from infrastructure.mysql import Base


class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    name = Column(String, unique=True)
    date = Column(String)
    content = Column(String)
    version = Column(Integer, default=1)
    previous_version = Column(Integer)


