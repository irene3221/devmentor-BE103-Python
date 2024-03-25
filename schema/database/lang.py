from sqlalchemy import Column, Integer, String
from infrastructure.mysql import Base


class Lang(Base):
    __tablename__ = 'langs'

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String)