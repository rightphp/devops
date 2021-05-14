FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-alpine3.10-2020-12-19

RUN apt-get install gcc

RUN pip3 install sqlalchemy pymysql motor pydantic[email] python-decouple

#COPY ./fastapi-mongo /app
COPY ./fastapideta /app