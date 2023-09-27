from fastapi.testclient import TestClient
from app.config import access

from main import app

client = TestClient(app)


def test_predict_gender_open():
    response = client.post(
        "/gender_detect_open/name/predict/",
        headers={"X-Token": "coneofsilence"},
        json={"name_input": ["Trần Văn A", "Nguyễn Thị B"]},
    )
    print(response.json())
    assert response.status_code == 200
    assert response.json() == ["male", "female"]


def test_predict_gender_authorize():
    response = client.post(
        "/gender_detect/name/predict/",
        headers={"Authorization": f'Bearer {access.BEARER_TOKEN}'},
        json={"name_input": ["Trần Văn A", "Nguyễn Thị B"]},
    )
    print(response.json())
    assert response.status_code == 200
    assert response.json() == ["male", "female"]


