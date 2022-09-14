from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.post_hashtag import PostHashtag
import schemas
import re


# 포스트-해시태그 생성 함수
async def post_hashtag_set(db: Session) -> PostHashtag:
    return True