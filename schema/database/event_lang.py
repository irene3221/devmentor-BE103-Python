from pydantic import BaseModel


class EventLangCreate(BaseModel):
    lang_id: int = 0
    content: str = ''


