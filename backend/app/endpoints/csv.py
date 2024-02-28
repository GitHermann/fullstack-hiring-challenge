from fastapi import APIRouter
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