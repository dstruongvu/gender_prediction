from fastapi import APIRouter
from app.api.api_v1.endpoints import access, gender_detect, gender_detect_open

api_router = APIRouter()
api_router.include_router(access.router)
api_router.include_router(gender_detect.router)
api_router.include_router(gender_detect_open.router)
