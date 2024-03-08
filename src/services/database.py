import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


if not os.path.exists('db'):
    os.makedirs('db')

SQLALCHEMY_DATABASE_URL = "sqlite:///db/db.sqlite3"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()
