from fastapi.testclient import TestClient
import requests
import os

from app.main import app

client = TestClient(app)

data_path = '../data'

def test_hello_world():
  response = client.get("/")
  assert response.status_code == 200
  assert response.json() == {"message": "Hello World"}

def test_get_all_datasets():
  response = client.get("/csv")
  assert response.status_code == 200
  assert response.json() == ["sample_data_01.csv", "sample_data_02.csv", "test_csv_file.csv"]

def test_post_csv():
  with open("test_csv_file.csv", "w") as test_csv_file:
    test_csv_file.write("invoice id, email, country, invoicing date, amount")

  with open("test_csv_file.csv", "rb") as test_csv_file:
    files = {"csv_file": test_csv_file}
    response = requests.post('http://127.0.0.1:8000/csv', files=files)
  
  os.remove("test_csv_file.csv")

  assert response.status_code == 200
  assert response.json() == {"message": "File test_csv_file.csv saved at data\\test_csv_file.csv", "id": "test_csv_file.csv"}

def test_get_dataset():
  response = client.get('/csv/test_csv_file')
  assert response.status_code == 200
  assert response.json() == {"file": "test_csv_file.csv", "size": 50}