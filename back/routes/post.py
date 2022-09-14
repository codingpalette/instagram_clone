from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from starlette.requests import Request
from sqlalchemy.orm import Session
from crud import crud_post, crud_hashtag, crud_post_hashtag

import schemas
from functions import func, token
from connection import get_db
from config import conf

config = conf()

router = APIRouter(
    prefix="/post",
)


# @router.post('', summary="포스트 작성")
# async def post_set(request: Request, post_data: schemas.PostSet, db: Session = Depends(get_db)):
#     aa = await crud_post.post_set(db, post_data)
#     bb = await crud_hashtag.hashtag_set(db)
#     cc = await crud_post_hashtag.post_hashtag_set(db)
#     return True
