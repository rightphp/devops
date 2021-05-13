import motor.motor_asyncio
from bson.objectid import ObjectId
from decouple import config

MONGO_DETAILS = config('MONGO_DETAILS') # read environment variable.

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.contacts
person_collection = database.get_collection("persons_collection")


# helpers


def person_helper(person) -> dict:
    return {
      "id": str(person["_id"]),
      "webhook_event": str(person["webhook_event"]),
      "query": str(person["query"]),
      "email_format": str(person["email_format"]),
      "person_first_name": str(person["person_first_name"]),
      "person_last_name": str(person["person_last_name"]),
      "person_headline": str(person["person_headline"]),
      "person_job_title": str(person["person_job_title"]),
      "person_location": str(person["person_location"]),
      "person_business_email": str(person["person_business_email"]),
      "person_personal_email": str(person["person_personal_email"]),
      "person_company_name": str(person["person_company_name"]),
      "person_city": str(person["person_city"]),
      "person_linkedin_id": str(person["person_linkedin_id"]),
      "person_linkedin_url": str(person["person_linkedin_url"]),
      "company_name": str(person["company_name"]),
      "company_founded": str(person["company_founded"]),
      "company_size": str(person["company_size"]),
      "company_type": str(person["company_type"]),
      "company_country": str(person["company_country"]),
      "company_industry": str(person["company_industry"]),
      "company_address": str(person["company_address"]),
      "company_linkedin_url": str(person["company_linkedin_url"]),
      "company_linkedin_id": str(person["company_linkedin_id"]),
      "company_meta_title": str(person["company_meta_title"]),
      "company_meta_description": str(person["company_meta_description"]),
      "company_meta_keywords": str(person["company_meta_keywords"]),
      "company_meta_phones": str(person["company_meta_phones"]),
      "company_meta_emails": str(person["company_meta_emails"])
    }

# crud operations

# Retrieve all persons present in the database
async def retrieve_persons():
    persons = []
    async for person in person_collection.find():
        persons.append(person_helper(person))
    return persons


# Add a new person into to the database
async def add_person(person_data: dict) -> dict:
    person = await person_collection.insert_one(person_data)
    new_person = await person_collection.find_one({"_id": person.inserted_id})
    return person_helper(new_person)


# Retrieve a person with a matching ID
async def retrieve_person(id: str) -> dict:
    person = await person_collection.find_one({"_id": ObjectId(id)})
    if person:
        return person_helper(person)


# Update a person with a matching ID
async def update_person(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    person = await person_collection.find_one({"_id": ObjectId(id)})
    if person:
        updated_person = await person_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_person:
            return True
        return False


# Delete a person from the database
async def delete_person(id: str):
    person = await person_collection.find_one({"_id": ObjectId(id)})
    if person:
        await person_collection.delete_one({"_id": ObjectId(id)})
        return True
