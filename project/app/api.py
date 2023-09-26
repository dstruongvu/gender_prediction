from fastapi import APIRouter
from router import access, gender_detect, gender_detect_open
# from .v1 import api_v1

api_router = APIRouter()
api_router.include_router(access.router)
api_router.include_router(gender_detect.router)
api_router.include_router(gender_detect_open.router)
