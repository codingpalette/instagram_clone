from sqlalchemy import Column, String, Integer, DateTime, Text, func, ForeignKey
from connection import Base
from sqlalchemy.orm import relationship

class Hashtag(Base):
    __tablename__ = "hashtag"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20), unique=True, index=True, nullable=True)
    created_at = Column(DateTime(6), default=func.utc_timestamp(), nullable=False)
    updated_at = Column(DateTime(6), default=func.utc_timestamp(), onupdate=func.utc_timestamp(), nullable=False)

    post_hashtag = relationship("PostHashtag", back_populates="hashtag")