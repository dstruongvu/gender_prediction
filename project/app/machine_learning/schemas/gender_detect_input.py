from typing import List, Optional, Dict
from pydantic import BaseModel


class GenderDetectNameInput(BaseModel):
    name_input: List[str] = []






