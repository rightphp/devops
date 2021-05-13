from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class ContactSchema(BaseModel):
    waiting: Optional[str]
    email_first: Optional[str]
    email_second: Optional[str]
    first_name: Optional[str]
    middle_name: Optional[str]
    last_name: Optional[str]
    url: Optional[str]
    job_title: Optional[str]
    company_name: Optional[str]
    company_domain: Optional[str]
    company_id: Optional[str]
    city: Optional[str]
    linkedin_id: Optional[str]
    owner: Optional[str]
    created_timestamp: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "waiting": "since 2 days",
                "email_first": "krishan@hirestorm.com",
                "email_second": "milpearl@gmail.com",
                "first_name": "John",
                "middle_name": "Doe",
                "last_name": "Saini",
                "url": "https://www.johndoe.com",
                "job_title": "Database Administrator",
                "company_name": "Alta Frisca",
                "company_domain": "http://www.altafrisca.com",
                "company_id": 324324,
                "city": "Motera",
                "linkedin_id": "http://www.linkedin.com/johndoe",
                "owner": 4570,
                "created_timestamp": 43554656
            }
        }


class UpdateContactModel(BaseModel):
    waiting: Optional[str]
    email_first: Optional[EmailStr]
    email_second: Optional[EmailStr]
    first_name: Optional[str]
    middle_name: Optional[str]
    last_name: Optional[str]
    url: Optional[str]
    job_title: Optional[str]
    company_name: Optional[str]
    company_domain: Optional[str]
    company_id: Optional[str]
    city: Optional[str]
    linkedin_id: Optional[str]
    owner: Optional[str]
    created_timestamp: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "waiting": "since 2 days",
                "email_first": "krishan@hirestorm.com",
                "email_second": "milpearl@gmail.com",
                "first_name": "John",
                "middle_name": "Doe",
                "last_name": "Saini",
                "url": "https://www.johndoe.com",
                "job_title": "Database Administrator",
                "company_name": "Alta Frisca",
                "company_domain": "http://www.altafrisca.com",
                "company_id": 324324,
                "city": "Motera",
                "linkedin_id": "http://www.linkedin.com/johndoe",
                "owner": 4570,
                "created_timestamp": 43554656,
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
