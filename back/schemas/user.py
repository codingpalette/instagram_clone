from typing import Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    pass


class UserSet(UserBase):
    email: str
    name: str
    nickname: str
    password: str
