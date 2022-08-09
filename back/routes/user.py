from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from starlette.requests import Request
from sqlalchemy.orm import Session
from connection import get_db
from config import conf
import schemas
import crud

config = conf()

router = APIRouter(
    prefix="/user",
)

@router.get('/test')
async def test():
    return True


@router.post('', summary="유저 생성")
async def user_set(request: Request, post_data: schemas.UserSet, db: Session = Depends(get_db)):
    return await crud.CRUDUser.user_set(db, post_data)