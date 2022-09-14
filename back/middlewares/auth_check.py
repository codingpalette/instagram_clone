from starlette.requests import Request
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from connection import get_db
import time


async def access_control(request: Request, call_next):
    # 미들웨어 시작 header 에서 쿠기를 가져온다
    print('미들웨어 시작')
    print(request.method)
    db: Session = Depends(get_db)
    print(db)
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    # response.headers["X-Process-Time"] = str(process_time)
    print(process_time)
    # response = await call_next(request)
    return response

