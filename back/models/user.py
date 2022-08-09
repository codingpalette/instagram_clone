from sqlalchemy import Column, String, Integer, DateTime, func
from connection import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, index=True, nullable=False)
    name = Column(String(30), nullable=False)
    nickname = Column(String(30), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    refresh_token = Column(String(255))
    created_at = Column(DateTime(6), default=func.utc_timestamp(), nullable=False)
    updated_at = Column(DateTime(6), default=func.utc_timestamp(), onupdate=func.utc_timestamp(), nullable=False)
    deleted_at = Column(DateTime(6))