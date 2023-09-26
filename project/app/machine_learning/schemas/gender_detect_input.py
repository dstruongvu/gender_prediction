from typing import List, Optional, Dict
from app.settings import generic as gns
from pydantic import BaseModel


class GenderDetectNameInput(BaseModel):
    name_input: List[str] = []






