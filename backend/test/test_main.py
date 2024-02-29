from fastapi.testclient import TestClient
import requests
import os

from app.main import app

client = TestClient(app)

data_path = '../data'
test_filename = 'test_csv_file.csv'
size = 0

def test_hello_world():
  response = client.get("/")
  assert response.status_code == 200
  assert response.json() == {"message": "Hello World"}

def test_get_all_datasets():
  response = client.get("/csv")
  assert response.status_code == 200
  assert response.json() == ["sample_data_01.csv", "sample_data_02.csv", test_filename]

def test_post_csv():
  with open(test_filename, "w") as test_csv_file:
    test_csv_file.write("invoice id, email, country, invoicing date, amount")

  with open(test_filename, "rb") as test_csv_file:
    global size
    size = os.path.getsize(test_filename)
    files = {"csv_file": test_csv_file}
    response = requests.post('http://127.0.0.1:8000/csv', files=files)
  
  os.remove(test_filename)

  assert response.status_code == 200
  assert response.json() == {"id": test_filename}

def test_get_dataset():
  response = client.get('/csv/test_csv_file')
  assert response.status_code == 200
  assert response.json() == {"file": test_filename, "size": size}