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
  return {"message": f"File '{csv_file.filename}' saved at '{file_path}'"}