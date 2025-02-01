from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_list_coins():
    response = client.get("/api/v1/coins", headers={"api-key": "your-secure-api-key"})
    assert response.status_code == 200
    assert isinstance(response.json()["data"], list)

def test_health_check():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"