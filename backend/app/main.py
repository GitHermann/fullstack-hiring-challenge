from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .endpoints import csv

app = FastAPI()

app.include_router(csv.router)

origins = ["http://localhost:5173"]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=['*'],
  allow_headers=['*'])

@app.get('/')
async def hello_world():
  return {"message": "Hello World"}