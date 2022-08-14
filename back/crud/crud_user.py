from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.user import User
import schemas


# 아이디 체크 함수
def user_id_get(db: Session, id: schemas.UserIdGet) -> User:
    try:
        return db.query(User).filter(User.id == id).first()
    except Exception as e:
        # print(e)
        raise HTTPException(status_code=500, detail={"result": "fail", "message": "서버에 문제가 발생했습니다"})


# 이메일로 가져오기
async def user_email_get(db: Session, email: schemas.UserEmailGet):
    try:
        return db.query(User).filter(User.email == email).first()
    except Exception as e:
        # print(e)
        raise HTTPException(status_code=500, detail={"result": "fail", "message": "서버에 문제가 발생했습니다"})


# 닉네임으로 가져오기
async def user_nickname_get(db: Session, nickname: schemas.UserNicknameGet):
    try:
        return db.query(User).filter(User.nickname == nickname).first()
    except Exception as e:
        # print(e)
        raise HTTPException(status_code=500, detail={"result": "fail", "message": "서버에 문제가 발생했습니다"})


async def user_set(db: Session, post_data: schemas.UserSet) -> User:
    try:
        db_obj = User(
            email=post_data.email,
            name=post_data.name,
            nickname=post_data.nickname,
            birthday=post_data.birthday,
            password=post_data.password,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    except Exception as e:
        # print(e)
        raise HTTPException(status_code=500, detail={"result": "fail", "message": "서버에 문제가 발생했습니다"})


async def token_update(db: Session, post_data: schemas.UserIdGet, refresh_token: str):
    try:
        user_info = user_id_get(db, post_data.id)
        user_info.refresh_token = refresh_token
        db.commit()
        db.refresh(user_info)

        return user_info

    except Exception as e:
        # print(e)
        raise HTTPException(status_code=500, detail={"result": "fail", "message": "서버에 문제가 발생했습니다"})
