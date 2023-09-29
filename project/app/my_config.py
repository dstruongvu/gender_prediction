from pydantic_settings import BaseSettings, SettingsConfigDict
from os.path import exists
import os
from typing import Optional

class Settings(BaseSettings):
    secret_key: str = ""
    algorithm: str = ""
    access_token_expire_minutes: int = 0
    bearer_token:str = ""
    log_config:dict = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if exists("./app/config/generic.py"):
            import app.config.generic as gns
            self.secret_key = gns.SECRET_KEY
            self.algorithm = gns.ALGORITHM
            self.access_token_expire_minutes = gns.ACCESS_TOKEN_EXPIRE_MINUTES
            self.bearer_token = gns.BEARER_TOKEN

settings = Settings()