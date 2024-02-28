from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_hello_world():
  response = client.get("/")
  assert response.status_code == 200
  assert response.json() == {"message": "Hello World"}

def test_get_all_datasets():
  response = client.get("/csv")
  assert response.status_code == 200
  assert response.json() == ["sample_data_01.csv"]