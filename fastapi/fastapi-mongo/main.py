'''
REFRENCES
https://testdriven.io/blog/fastapi-mongo/
https://testdriven.io/courses/tdd-fastapi/
https://hub.docker.com/r/tiangolo/uvicorn-gunicorn-fastapi
https://fastapi.tiangolo.com/advanced/nosql-databases/?h=mongo#add-a-function-to-get-a-bucket
https://plugins.jenkins.io/amazon-ecs/
https://plugins.jenkins.io/amazon-ecs/
https://medium.com/analytics-vidhya/how-to-deploy-a-python-api-with-fastapi-with-nginx-and-docker-1328cbf41bc
'''

from fastapi import FastAPI

from app.server.routes.contact import router as ContactRouter
from app.server.routes.person import router as PersonRouter

app = FastAPI()

app.include_router(ContactRouter, tags=["Contact"], prefix="/contact")
app.include_router(PersonRouter, tags=["Person"], prefix="/person")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}
