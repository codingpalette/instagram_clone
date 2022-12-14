from fastapi import HTTPException
from functions import token


# 유저 검증 함수
async def login_info_get(request):
    cookies = request.cookies
    access_token = cookies.get("access_token")
    refresh_token = cookies.get("refresh_token")
    if not access_token:
        return False

    login_info = await token.token_check(access_token, refresh_token)
    print('12313')

    if not login_info:
        return False

    return login_info
