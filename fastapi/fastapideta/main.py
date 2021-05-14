'''
REFRENCES
https://testdriven.io/blog/fastapi-mongo/
https://testdriven.io/courses/tdd-fastapi/
https://hub.docker.com/r/tiangolo/uvicorn-gunicorn-fastapi
https://fastapi.tiangolo.com/advanced/nosql-databases/?h=mongo#add-a-function-to-get-a-bucket
https://plugins.jenkins.io/amazon-ecs/
https://medium.com/analytics-vidhya/how-to-deploy-a-python-api-with-fastapi-with-nginx-and-docker-1328cbf41bc
'''

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}