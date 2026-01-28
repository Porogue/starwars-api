from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_main():
    response = client.get("/get/1")
    assert response.status_code == 200