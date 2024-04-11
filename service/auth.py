from database.user import UserWithPassword
from sqlalchemy.orm import Session
from repository.user import get_user

def validate_login(db: Session, form_data_username: str, form_data_password: str) -> UserWithPassword:
    user = get_user(db, form_data_username)
    if not user:
        return None
    if not form_data_password == user.password:
        return False
    return user