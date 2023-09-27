from fastapi import Body, FastAPI, Form, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Depends, FastAPI
from datetime import timedelta
from app.api.api_v1.api import api_router
# from app.controller.access import create_access_token
# from app.models.simple_users import fake_users_db

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

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.include_router(api_router)


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("home.html", context={"request": request})



