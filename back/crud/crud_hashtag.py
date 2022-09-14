from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.hashtag import Hashtag
import schemas
import re


# 해시태그 생성 함수
async def hashtag_set(db: Session) -> Hashtag:
    return True