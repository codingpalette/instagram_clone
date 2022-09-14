from sqlalchemy import Column, String, Integer, DateTime, func, PickleType, ForeignKey
from connection import Base
from sqlalchemy.orm import relationship

class PostHashtag(Base):
    __tablename__ = "post_hashtag"

    id = Column(Integer, primary_key=True, index=True)
    hashtag_id = Column(Integer, ForeignKey("hashtag.id",  ondelete='CASCADE'), nullable=False)
    post_id = Column(Integer, ForeignKey("post.id", ondelete='CASCADE'), nullable=False)
    created_at = Column(DateTime(6), default=func.utc_timestamp(), nullable=False)
    updated_at = Column(DateTime(6), default=func.utc_timestamp(), onupdate=func.utc_timestamp(), nullable=False)

    # hashtag = relationship("Hashtag", back_populates="post_hashtag")
    # post = relationship("Post", back_populates="post_hashtag")