from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, validator, Field


class User(BaseModel):
    id: Optional[str] = None
    username: str
    email: str
    password: str
