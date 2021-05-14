FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-alpine3.10-2020-12-19

#RUN apk --update-cache add gcc

#RUN pip3 install sqlalchemy pymysql motor pydantic[email] python-decouple

RUN pip install --no-cache-dir fastapi

#COPY ./fastapi-mongo /app
COPY ./fastapideta /app
