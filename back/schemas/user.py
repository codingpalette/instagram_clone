from typing import Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    pass


class UserIdGet(UserBase):
    id: str


class UserEmailGet(UserBase):
    email: str


class UserNicknameGet(UserBase):
    nickname: str


class UserSet(UserBase):
    email: str
    name: str
    nickname: str
    password: str
    birthday: str


class UserLogin(UserBase):
    email: str
    password: str
