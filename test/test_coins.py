from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_list_coins():
    response = client.get("/coins?page_num=1&per_page=10")
    assert response.status_code == 200
    assert len(response.json()) == 10
