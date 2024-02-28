from fastapi import FastAPI

from .endpoints import csv

app = FastAPI()

app.include_router(csv.router)

@app.get('/')
async def hello_world():
  return {"message": "Hello World"}