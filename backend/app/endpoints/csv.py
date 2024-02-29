from fastapi import APIRouter, UploadFile, Response, status
import os
import pandas as pd
import json

data_path = 'data'

router = APIRouter()

@router.get('/csv')
async def get_all_datasets():
  '''
    Returns the file name of all csv files
  '''
  return list_csv_files(data_path)

def list_csv_files(path : str):
  csv_files = [file for file in os.listdir(path) if file.endswith('.csv')]
  return csv_files

@router.post('/csv', status_code= 201)
async def post_csv(csv_file: UploadFile):
  '''
    Saves a copy of the uploaded csv file into the file system
  '''
  file_path = os.path.join(data_path, csv_file.filename)

  with open(file_path, 'wb+') as new_file:
    new_file.write(csv_file.file.read())
  return {"id": csv_file.filename}

def find_file_if_exists(filename: str):
  for file in list_csv_files(data_path):
    if file == filename:
      return file
  return

@router.get('/csv/{id}', status_code=404)
async def get_dataset(id: str, response: Response):
  '''
    Returns the file name and the size of the dataset
  '''
  filename = id + '.csv'
  file = find_file_if_exists(filename)
  if file is not None:
    response.status_code = status.HTTP_200_OK
    return {"file": file,  "size": os.path.getsize(os.path.join(data_path,filename))}
  else:
    return

@router.delete('/csv/{id}', status_code=404)
async def delete_dataset(id: str, response: Response):
  '''
    Deletes the dataset
  '''
  filename = id + '.csv'
  file = find_file_if_exists(filename)
  if file is not None:
    os.remove(os.path.join(data_path,filename))
    response.status_code == status.HTTP_200_OK
    return {"message": "File removed"}
  else:
    return

def csv_to_json(csv_file: str):
  df = pd.read_csv(csv_file, sep=";")
  df.columns = df.columns.str.strip()
  df_grouped = df.groupby(['email'])
  emails = []
  payments = []

  for name, group in df_grouped:
    emails.append(name[0])
    payments.append(group[['invoicing date', 'amount']].to_dict())

  return {"emails": emails, "payments": payments}

@router.get('/csv/{id}/plot', status_code=404)
async def get_amount_per_customer_per_month(id: str, response: Response):
  '''
    Returns a formatted dataset containing the amount paid by each customer per month
  '''
  filename = id + '.csv'
  file = find_file_if_exists(filename)
  if file is not None:
    formatted_dataset = csv_to_json(os.path.join(data_path,file))
    response.status_code = status.HTTP_200_OK
    return formatted_dataset
  else:
    return