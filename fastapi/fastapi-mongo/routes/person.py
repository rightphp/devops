from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

# folowing is for logging
from fastapi.logger import logger
import logging
import sys
import traceback

gunicorn_logger = logging.getLogger('gunicorn.error')
logger.handlers = gunicorn_logger.handlers
if __name__ != "main":
    logger.setLevel(gunicorn_logger.level)
else:
    logger.setLevel(logging.DEBUG)

#above is for logging

from person_database import (
    add_person,
    delete_person,
    retrieve_person,
    retrieve_persons,
    update_person,
)
from models.person import (
    ErrorResponseModel,
    ResponseModel,
    PersonSchema,
    UpdatePersonModel,
)

router = APIRouter()

    

    

try:
 @router.post("/", response_description="Person data added into the database")
 async def add_person_data(person: PersonSchema = Body(...)):
    person = jsonable_encoder(person)
    new_person = await add_person(person)
    return ResponseModel(new_person, "Person added successfully.")
except Exception as e: # catch *all* exceptions
 ERROR = "CAN TR VerifyEmail Error@TrueMail: " + str(e)
 val = traceback.format_exc()
 TRACES = "CAND TR VerifyEmail Traces@TrueMail: %s" % val.replace('"', "'")
 logger.info(ERROR)
 logger.info(TRACES)

@router.get("/", response_description="Persons retrieved")
async def get_persons():
    persons = await retrieve_persons()
    if persons:
        return ResponseModel(persons, "Persons data retrieved successfully")
    return ResponseModel(persons, "Empty list returned")


@router.get("/{id}", response_description="Person data retrieved")
async def get_person_data(id):
    person = await retrieve_person(id)
    if person:
        return ResponseModel(person, "Person data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Person doesn't exist.")


@router.put("/{id}")
async def update_person_data(id: str, req: UpdatePersonModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_person = await update_person(id, req)
    if updated_person:
        return ResponseModel(
            "Person with ID: {} name update is successful".format(id),
            "Person name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the person data.",
    )


@router.delete("/{id}", response_description="Person data deleted from the database")
async def delete_person_data(id: str):
    deleted_person = await delete_person(id)
    if deleted_person:
        return ResponseModel(
            "Person with ID: {} removed".format(id), "Person deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Person with id {0} doesn't exist".format(id)
    )
