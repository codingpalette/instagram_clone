from config import conf
from dotmap import DotMap
import datetime
import jwt
from sqlalchemy.orm import Session
from connection import get_db
from crud import crud_user

config = conf()


# 토큰 생성 함수
def create_token(type, user_info):
    key = config['TOKEN_KEY']
    alg = 'HS256'
    # days->날짜 hours->시간, minutes->분, seconds->초
    payload = {
        "id": user_info.id,
        "email": user_info.email,
        "name": user_info.name,
        "nickname": user_info.nickname,
    }
    if type == "access_token":
        payload["exp"] = datetime.datetime.utcnow() + datetime.timedelta(days=1)
    else:
        payload["exp"] = datetime.datetime.utcnow() + datetime.timedelta(days=14)

    return jwt.encode(payload=payload, key=key, algorithm=alg)


# 토큰 체크
async def token_check(access_token, refresh_token):
    try:
        # print(access_token)
        # print(refresh_token)
        key = config['TOKEN_KEY']
        # access_token 으로 검사를 하고 맞으면 통과 기간이 지났으면 refresh_token 으로 검사를 해준다.
        jwt.decode(access_token, key, algorithms=['HS256'])
        return access_token
    except jwt.ExpiredSignatureError:
        # 그래서 유효시간이 지난 토큰 에러인 'ExpiredSignatureError' 를 먼저 잡습니다.
        # refresh_token 으로 실제 디비에 refresh_token의 유저를 가져온다
        try:
            key = config['TOKEN_KEY']
            # refresh_token 을 검사 하고 기간이 지나면 실패한다
            # 성공일 경우 새로운 access_token 을 발급해 준다.
            # print('갱신 시작')
            decode = jwt.decode(refresh_token, key, algorithms=['HS256'])
            # print(decode)
            user_info = DotMap()
            user_info.id = decode["id"]
            user_info.email = decode["email"]
            user_info.name = decode["name"]
            user_info.nickname = decode["nickname"]
            return create_token('access_token', user_info)
        except jwt.ExpiredSignatureError:
            return False

    except jwt.InvalidTokenError:
        # 유효시간이 지났는지, signature가 맞지 않는지에 상관없이 유효하지 않은 토큰인 경우 모두 잡아냅니다.
        return False

