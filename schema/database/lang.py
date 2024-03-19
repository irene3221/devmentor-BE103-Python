from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Lang(Base):
    __tablename__ = 'langs'

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String)