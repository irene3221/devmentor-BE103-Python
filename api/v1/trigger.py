from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

import repository.trigger
import repository.event
from infrastructure.mysql import get_db

router = APIRouter(
    tags=["trigger"],
    prefix="/trigger-event"
)

@router.get("/{event_id}")
def trigger(event_id: int, db: Session = Depends(get_db)):
    user_list = repository.trigger.get_user_subscribe(db, event_id)
    event = repository.event.get_event(db, event_id)
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    else:
        previous_event_version = repository.event.get_previous_event_state(db, event_id)
        if event.version != previous_event_version:
            user_list_dict = [user_id for user_id, in user_list]
            event_dict = {"id": event.id, "name": event.name, "date": event.date, "content": event.content}
            return {"user_list": user_list_dict, "event": event_dict}
        else:
            return "no update"
