from config import conf
from dotmap import DotMap
import datetime
import jwt
config = conf()


# 엑세스 토큰 체크
async def access_token_check(access_token):
    try:
        key = config['TOKEN_KEY']
        decode = jwt.decode(access_token, key, algorithms=['HS256'])
        return decode
    except Exception as e:
        # print(e)
        return False