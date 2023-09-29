from fastapi.testclient import TestClient
from app.my_config import settings

from main import app

client = TestClient(app)


def test_predict_gender_open():
    response = client.post(
        "/gender_detect_open/name/predict/",
        headers={"X-Token": "coneofsilence"},
        json={"name_input": ["Trần Văn A", "Nguyễn Thị B"]},
    )
    assert response.status_code == 200
    assert response.json() == ["male", "female"]


def test_predict_gender_authorize():
    response = client.post(
        "/gender_detect/name/predict/",
        headers={"Authorization": f'Bearer {settings.bearer_token}'},
        json={"name_input": ["Trần Văn A", "Nguyễn Thị B"]},
    )
    print('TruongVV-----------', settings.bearer_token)
    assert response.status_code == 200
    assert response.json() == ["male", "female"]


