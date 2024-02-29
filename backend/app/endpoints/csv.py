from fastapi import APIRouter, UploadFile
import os

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

@router.post('/csv')
async def post_csv(csv_file: UploadFile):
  '''
    Saves a copy of the uploaded csv file into the file system
  '''
  file_path = os.path.join(data_path, csv_file.filename)

  with open(file_path, 'wb+') as new_file:
    new_file.write(csv_file.file.read())
  return {"id": csv_file.filename}

@router.get('/csv/{id}')
async def get_dataset(id: str):
  '''
    Returns the file name and the size of the dataset
  '''
  filename = id + '.csv'
  for file in list_csv_files(data_path):
    if file == filename:
      return {"file": file,  "size": os.path.getsize(os.path.join(data_path,filename))}
  return