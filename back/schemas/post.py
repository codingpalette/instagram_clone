from typing import Optional
from pydantic import BaseModel


class PostSet(BaseModel):
    user_id: int
    content: str


