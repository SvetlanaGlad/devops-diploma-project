from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Welcome to my Research Project",
        "status": "Ready"}


def test_healt_check():
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json()["status"] == "UP"


def test_system_metrics():
    response = client.get("/system")
    assert response.status_code == 200
    assert "cpu_load" in response.json()
    assert "memory_load" in response.json()
