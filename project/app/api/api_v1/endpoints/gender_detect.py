from fastapi import APIRouter, Depends, Body
from fastapi.responses import JSONResponse
import json
from typing_extensions import Annotated

from app.controller.access import get_current_active_user, verify_token
from app.machine_learning.schemas.gender_detect_input import GenderDetectNameInput
from app.machine_learning.controller.gender_detect import GenderDetectionNameBayes

from app.logging.my_log_route import LogRoute


router = APIRouter(
    prefix="/gender_detect/name",
    tags=["gender_detect"],
    dependencies=[Depends(verify_token)],
    responses={404: {"description": "Not found"}},
    route_class=LogRoute
)

example_name_input = {"name_input": ["Trần Văn A", "Nguyễn Thị B"]}

@router.post("/predict_prob")
def predict(c_input: Annotated[
                        GenderDetectNameInput,
                        Body(examples=example_name_input)
                    ]):
    t = GenderDetectionNameBayes().predict_prob(c_input)
    return JSONResponse(t)


@router.post("/predict")
def predict(c_input: Annotated[
                                GenderDetectNameInput, 
                                Body(examples=example_name_input)
                            ]):
    t = GenderDetectionNameBayes().predict(c_input)
    return JSONResponse(t)


