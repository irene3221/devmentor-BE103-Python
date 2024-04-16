from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
import service.event
import repository.trigger
import repository.event
from infrastructure.mysql import get_db
from service.email import EmailService
from service.line import LineService
from service.telegram import TelegramService

router = APIRouter(
    tags=["trigger"],
    prefix="/trigger-event"
)

@router.get("/{event_id}")
def trigger(event_id: int, lang_id: int, db: Session = Depends(get_db)):
    users = repository.trigger.get_user_subscribe(db, event_id)
    users = [user[0] for user in users]
    content = service.event.get_content_by_id(db, event_id, lang_id)
    if content is None:
        raise HTTPException(status_code=404, detail="Event not found")
    TelegramService().send(db, users, content)
    EmailService().send(db, users, content)
    LineService().send(db, users, content)