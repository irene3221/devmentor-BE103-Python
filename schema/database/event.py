from typing import Optional

from pydantic import BaseModel

class EventBase(BaseModel):
    user_id: int = 0
    name: str = ''
    date: str =''

class EventCreate(BaseModel):
    name: str
    date: str

class Event(EventBase):
    id: int


class EventUpdate(BaseModel):
    name: Optional[str]
    date: Optional[str]


    class Config:
        orm_mode = True
