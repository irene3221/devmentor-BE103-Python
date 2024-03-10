from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Notification(Base):
    __tablename__ = 'notifications'

    id = Column(Integer, primary_key=True)
    message_key = Column(String)
    message = Column(String)
    language_id = Column(Integer, ForeignKey('languages.id'))

engine = create_engine("mysql+pymysql://admin:1234@127.0.0.1:3306/be103")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

class NotificationSystem:
    def __init__(self, language):
        self.language = language

    def get_notification(self, message_key):
        notification = session.query(Notification).filter_by(message_key=message_key, language_id=self.language).first()
        return notification.message if notification else f"No message found for key '{message_key}'"


