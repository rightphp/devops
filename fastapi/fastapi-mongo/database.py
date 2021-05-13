import motor.motor_asyncio
from bson.objectid import ObjectId
from decouple import config

MONGO_DETAILS = config('MONGO_DETAILS') # read environment variable.

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.contacts
contact_collection = database.get_collection("contacts_collection")


# helpers


def contact_helper(contact) -> dict:
    return {
        "id": str(contact["_id"]),
        "waiting": contact["waiting"],
        "email_first": contact["email_first"],
        "email_second": contact["email_second"],
        "first_name": contact["first_name"],
        "middle_name": contact["middle_name"],
		"last_name": contact["last_name"],
		"url": contact["url"],
		"job_title": contact["job_title"],
		"company_name": contact["company_name"],
		"company_domain": contact["company_domain"],
		"company_id": contact["company_id"],
		"city": contact["city"],
		"linkedin_id": contact["linkedin_id"],
		"owner": contact["owner"],
		"created_timestamp": contact["created_timestamp"]
    }

# crud operations

# Retrieve all contacts present in the database
async def retrieve_contacts():
    contacts = []
    async for contact in contact_collection.find():
        contacts.append(contact_helper(contact))
    return contacts


# Add a new contact into to the database
async def add_contact(contact_data: dict) -> dict:
    contact = await contact_collection.insert_one(contact_data)
    new_contact = await contact_collection.find_one({"_id": contact.inserted_id})
    return contact_helper(new_contact)


# Retrieve a contact with a matching ID
async def retrieve_contact(id: str) -> dict:
    contact = await contact_collection.find_one({"_id": ObjectId(id)})
    if contact:
        return contact_helper(contact)


# Update a contact with a matching ID
async def update_contact(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    contact = await contact_collection.find_one({"_id": ObjectId(id)})
    if contact:
        updated_contact = await contact_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_contact:
            return True
        return False


# Delete a contact from the database
async def delete_contact(id: str):
    contact = await contact_collection.find_one({"_id": ObjectId(id)})
    if contact:
        await contact_collection.delete_one({"_id": ObjectId(id)})
        return True
