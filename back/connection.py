from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base  # Base 생성
from config import conf

config = conf()
SQLALCHEMY_DATABASE_URL = f'''{config['DATABASE_TYPE']}://{config['USERNAME']}:{config['PASSWORD']}@{config['HOST']}:3306/{config['DATABASE']}'''
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()