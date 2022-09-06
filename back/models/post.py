from sqlalchemy import Column, String, Integer, DateTime, Text, func, ForeignKey
from connection import Base
from sqlalchemy.orm import relationship

class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id", ondelete='CASCADE'), nullable=False)
    content = Column(Text)
    created_at = Column(DateTime(6), default=func.utc_timestamp(), nullable=False)
    updated_at = Column(DateTime(6), default=func.utc_timestamp(), onupdate=func.utc_timestamp(), nullable=False)

    user = relationship("User", back_populates="post")

    post_hashtag = relationship("PostHashtag", back_populates="post")