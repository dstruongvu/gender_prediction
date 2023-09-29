from pydantic import BaseModel
from typing import Optional


class SimpleUser(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None


class SimpleUserInDB(SimpleUser):
    hashed_password: str
