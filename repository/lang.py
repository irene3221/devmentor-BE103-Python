from sqlalchemy.orm import Session

from schema.database.lang import Lang

def choose_lang(db: Session, lang_id: int):
    return db.query(Lang).filter(Lang.id == lang_id).first()