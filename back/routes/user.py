from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from starlette.requests import Request
from sqlalchemy.orm import Session
from connection import get_db
from functions import func
from config import conf
import schemas
import bcrypt
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

    # 로그인 여부 확인
    login_info = await func.login_info_get(request)
    if login_info:
        raise HTTPException(status_code=401, detail={"result": "fail", "message": "로그아웃 후 이용해 주세요."})

    # 이메일 체크
    login_email_info = await crud.CRUDUser.user_email_get(db, post_data.email)
    if login_email_info:
        raise HTTPException(status_code=401, detail={"result": "fail", "message": "이미 사용중인 이메일 입니다."})

    # 닉네임 체크
    login_nickname_info = await crud.CRUDUser.user_nickname_get(db, post_data.nickname)
    if login_nickname_info:
        raise HTTPException(status_code=401, detail={"result": "fail", "message": "이미 사용중인 닉네임 입니다."})

    # 비밀번호 암호화
    hashed_password = bcrypt.hashpw(post_data.password.encode('utf-8'), bcrypt.gensalt())
    save_password = hashed_password.decode('utf-8')
    post_data.password = save_password
    save_user = await crud.CRUDUser.user_set(db, post_data)
    if save_user:
        return JSONResponse(status_code=201, content={"result": "success", "message": "회원가입에 성공 했습니다"})
    else:
        raise HTTPException(status_code=501, detail={"result": "fail", "message": "회원가입에 실패 했습니다."})

