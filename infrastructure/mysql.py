from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://admin:1234@mysql80/be103"
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://admin:1234@127.0.0.1:3308/be103"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, echo=True,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
