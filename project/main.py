from fastapi import Body, FastAPI, Form, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Depends, FastAPI
from datetime import timedelta
from functools import lru_cache
from app.api.api_v1.api import api_router
from app.my_config import Settings

description = """
Data API helps you do awesome stuff.
"""

app = FastAPI(
    title="Test API",
    description=description,
    version="1",
    terms_of_service="",
    contact={
        "name": "Test team",
        "email": "truongvv@gmail.com",
    },
    license_info={
        "name": "truongvv@gmail.com",
    },
)

@lru_cache()
def get_settings():
    return Settings()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.include_router(api_router)


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("home.html", context={"request": request})



