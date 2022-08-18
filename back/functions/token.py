from config import conf
from dotmap import DotMap
import datetime
import jwt

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


# 엑세스 토큰 체크
async def access_token_check(access_token):
    try:
        key = config['TOKEN_KEY']
        decode = jwt.decode(access_token, key, algorithms=['HS256'])
        return decode
    except Exception as e:
        # print(e)
        return False
