from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.database import (
    add_contact,
    delete_contact,
    retrieve_contact,
    retrieve_contacts,
    update_contact,
)
from app.server.models.contact import (
    ErrorResponseModel,
    ResponseModel,
    ContactSchema,
    UpdateContactModel,
)

router = APIRouter()


@router.post("/", response_description="Contact data added into the database")
async def add_contact_data(contact: ContactSchema = Body(...)):
    contact = jsonable_encoder(contact)
    new_contact = await add_contact(contact)
    return ResponseModel(new_contact, "Contact added successfully.")


@router.get("/", response_description="Contacts retrieved")
async def get_contacts():
    contacts = await retrieve_contacts()
    if contacts:
        return ResponseModel(contacts, "Contacts data retrieved successfully")
    return ResponseModel(contacts, "Empty list returned")


@router.get("/{id}", response_description="Contact data retrieved")
async def get_contact_data(id):
    contact = await retrieve_contact(id)
    if contact:
        return ResponseModel(contact, "Contact data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Contact doesn't exist.")


@router.put("/{id}")
async def update_contact_data(id: str, req: UpdateContactModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_contact = await update_contact(id, req)
    if updated_contact:
        return ResponseModel(
            "Contact with ID: {} name update is successful".format(id),
            "Contact name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the contact data.",
    )


@router.delete("/{id}", response_description="Contact data deleted from the database")
async def delete_contact_data(id: str):
    deleted_contact = await delete_contact(id)
    if deleted_contact:
        return ResponseModel(
            "Contact with ID: {} removed".format(id), "Contact deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Contact with id {0} doesn't exist".format(id)
    )
