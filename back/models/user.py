from sqlalchemy import Column, String, Integer, DateTime, func
from connection import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100))
    name = Column(String(30))
    nickname = Column(String(30))
    password = Column(String(255))
    sns_id = Column(String(255), unique=True, index=True)
    login_type = Column(String(100), default="homepage")
    birthday = Column(DateTime(6))
    refresh_token = Column(String(255))
    created_at = Column(DateTime(6), default=func.utc_timestamp(), nullable=False)
    updated_at = Column(DateTime(6), default=func.utc_timestamp(), onupdate=func.utc_timestamp(), nullable=False)
    deleted_at = Column(DateTime(6))
