from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.post import Post
import schemas
import re


# 포스트 생성 함수
async def post_set(db: Session, post_data: schemas.PostSet) -> Post:
    print(post_data)
    regex = re.compile("#([0-9a-zA-Z가-힣]*)")
    tag = regex.findall(post_data.content)
    print(tag)
    return True
