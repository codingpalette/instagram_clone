from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from starlette.requests import Request
from sqlalchemy.orm import Session
from functions import func, token
from connection import get_db
from crud import crud_user
from config import conf
import schemas
import bcrypt
import datetime


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
    login_email_info = await crud_user.user_email_get(db, post_data.email)
    if login_email_info:
        raise HTTPException(status_code=401, detail={"result": "fail", "message": "이미 사용중인 이메일 입니다."})

    # 닉네임 체크
    login_nickname_info = await crud_user.user_nickname_get(db, post_data.nickname)
    if login_nickname_info:
        raise HTTPException(status_code=401, detail={"result": "fail", "message": "이미 사용중인 닉네임 입니다."})

    # 비밀번호 암호화
    hashed_password = bcrypt.hashpw(post_data.password.encode('utf-8'), bcrypt.gensalt())
    save_password = hashed_password.decode('utf-8')
    post_data.password = save_password
    save_user = await crud_user.user_set(db, post_data)
    if save_user:
        return JSONResponse(status_code=201, content={"result": "success", "message": "회원가입에 성공 했습니다"})
    else:
        raise HTTPException(status_code=501, detail={"result": "fail", "message": "회원가입에 실패 했습니다."})


@router.post('/login', summary="유저 로그인")
async def user_login(request: Request, post_data: schemas.UserLogin, db: Session = Depends(get_db)):

    # 로그인 여부 확인
    login_info = await func.login_info_get(request)
    if login_info:
        raise HTTPException(status_code=401, detail={"result": "fail", "message": "로그아웃 후 이용해 주세요."})

    # 이메일 체크
    login_id_info = await crud_user.user_email_get(db, post_data.email)
    if not login_id_info:
        raise HTTPException(status_code=401, detail={"result": "fail", "message": "존재하지 않는 이메일 입니다."})

    # 패스워드 체크
    password_check = bcrypt.checkpw(post_data.password.encode('utf-8'), login_id_info.password.encode('utf-8'))
    if not password_check:
        raise HTTPException(status_code=401, detail={"result": "fail", "message": "비밀번호가 틀립니다."})

    # 토큰 만들기
    access_token = token.create_token('access_token', login_id_info)
    refresh_token = token.create_token('refresh_token', login_id_info)

    # db에 토큰 업데이트
    token_update = await crud_user.token_update(db, login_id_info, refresh_token)

    if token_update:
        access_token_time = datetime.datetime.utcnow() + datetime.timedelta(days=1)
        refresh_token_time = datetime.datetime.utcnow() + datetime.timedelta(days=14)
        content = {"result": "success", "message": "로그인 성공"}
        response = JSONResponse(content=content)
        response.set_cookie(
            key="access_token",
            value=access_token,
            secure=True,
            httponly=True,
            expires=access_token_time.strftime("%a, %d %b %Y %H:%M:%S GMT"),
        )
        response.set_cookie(
            key="refresh_token",
            value=refresh_token,
            secure=True,
            httponly=True,
            expires=refresh_token_time.strftime("%a, %d %b %Y %H:%M:%S GMT"),
        )
        return response
    else:
        raise HTTPException(status_code=501, detail={"result": "fail", "message": "로그인에 실패했습니다."})
