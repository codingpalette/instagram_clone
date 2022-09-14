from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.user import User
import schemas


# 아이디 체크 함수
def user_id_get(db: Session, id: schemas.UserIdGet) -> User:
    try:
        return db.query(User).filter(User.id == id).first()
    except Exception as e:
        raise HTTPException(status_code=500, detail={"result": "fail", "message": "서버에 문제가 발생했습니다"})


# 이메일로 가져오기
async def user_email_get(db: Session, email: schemas.UserEmailGet):
    print(email)
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


# 유저 저장
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
        print(e)
        raise HTTPException(status_code=500, detail={"result": "fail", "message": "서버에 문제가 발생했습니다"})


# 리프레쉬 토큰 업데이트
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


# 리프레쉬 토큰으로 유저 가지고 오기
async def user_refresh_token_get(db: Session, refresh_token: str) -> User:
    try:
        return db.query(User).filter(User.refresh_token == refresh_token).first()
    except Exception as e:
        raise HTTPException(status_code=500, detail={"result": "fail", "message": "서버에 문제가 발생했습니다"})


# 유저 로그아웃
async def log_out(db: Session, id: int) -> User:
    try:
        user_info = user_id_get(db, id)
        user_info.refresh_token = None
        db.commit()
        db.refresh(user_info)

        return user_info

    except Exception as e:
        raise HTTPException(status_code=500, detail={"result": "fail", "message": "서버에 문제가 발생했습니다"})


# kakao 유저 검색
async def kakao_user_get(db: Session, sns_id: int) -> User:
    try:
        return db.query(User).filter(User.sns_id == sns_id, User.login_type == 'kakao').first()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail={"result": "fail", "message": "서버에 문제가 발생했습니다"})

# kakao 유저 등록
async def kakao_set(db: Session, post_data) -> User:
    try:
        # print(post_data)
        # return True
        # add_insert = []
        # if "email" in post_data["kakao_account"]:
        #     add_insert.append(email = post_data["kakao_account"]["email"])

        db_obj = User(
            sns_id=post_data["id"],
            login_type="kakao",
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail={"result": "fail", "message": "서버에 문제가 발생했습니다"})
