from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_search_users():
    response = client.get("api/v1/users/?skip=0&limit=10")
    assert response.status_code == 200
    assert isinstance(response.json(), list)