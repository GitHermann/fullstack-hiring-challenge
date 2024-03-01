# fullstack-hiring-challenge

## Requirements

### Backend

- Python 3.12 or higher

- fastAPI and all its dependencies

 ``` shell
pip install "fastapi[all]"
```

- pandas

``` shell
pip install pandas
```

- poetry

### Frontend

- Vue.js

- npm

## Launching the Python API server

We created a poetry virtual environment containing fastAPI and pandas. Activate it with

``` shell
$/backend/> poetry shell
```

Then launch the backend with

``` shell
$/backend/> uvicorn app.main:app
```

It should be accessible on localhost:8000

## Launching the front app

Run the following commands

``` shell
$/frontend/app> npm install
$/frontend/app> npm run dev
```

The front app should be accessible on localhost:5173
