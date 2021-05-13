from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class PersonSchema(BaseModel):
    query: str = Field(...)
    email_format: Optional[str]
    person_first_name: Optional[str]
    person_last_name: Optional[str]
    person_headline: Optional[str]
    person_job_title: Optional[str]
    person_location: Optional[str]
    person_business_email: Optional[str]
    person_personal_email: Optional[str]
    person_company_name: Optional[str]
    person_city: Optional[str]
    person_linkedin_id: Optional[str]
    person_linkedin_url: Optional[str]
    company_name: Optional[str]
    company_founded: Optional[str]
    company_size: Optional[str]
    company_type: Optional[str]
    company_country: Optional[str]
    company_industry: Optional[str]
    company_address: Optional[str]
    company_linkedin_url: Optional[str]
    company_linkedin_id: Optional[str]
    company_meta_title: Optional[str]
    company_meta_description: Optional[str]
    company_meta_keywords: Optional[str]
    company_meta_phones: Optional[str]
    company_meta_emails: Optional[str]
    webhook_event: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "query": "xxx",
                "email_format": "value",
                "person_first_name": "value",
                "person_last_name": "value",
                "person_headline": "value",
                "person_job_title": "value",
                "person_location": "value",
                "person_business_email": "value",
                "person_personal_email": "value",
                "person_company_name": "value",
                "person_city": "value",
                "person_linkedin_id": "value",
                "person_linkedin_url": "value",
                "company_name": "value",
                "company_founded": "value",
                "company_size": "value",
                "company_type": "value",
                "company_country": "value",
                "company_industry": "value",
                "company_address": "value",
                "company_linkedin_url": "value",
                "company_linkedin_id": "value",
                "company_meta_title": "value",
                "company_meta_description": "value",
                "company_meta_keywords": "value",
                "company_meta_phones": "value",
                "company_meta_emails": "value",
                "webhook_event": "new_enrichment_found"
}
        }


class UpdatePersonModel(BaseModel):
    query: str = Field(...)
    email_format: Optional[str]
    person_first_name: Optional[str]
    person_last_name: Optional[str]
    person_headline: Optional[str]
    person_job_title: Optional[str]
    person_location: Optional[str]
    person_business_email: Optional[str]
    person_personal_email: Optional[str]
    person_company_name: Optional[str]
    person_city: Optional[str]
    person_linkedin_id: Optional[str]
    person_linkedin_url: Optional[str]
    company_name: Optional[str]
    company_founded: Optional[str]
    company_size: Optional[str]
    company_type: Optional[str]
    company_country: Optional[str]
    company_industry: Optional[str]
    company_address: Optional[str]
    company_linkedin_url: Optional[str]
    company_linkedin_id: Optional[str]
    company_meta_title: Optional[str]
    company_meta_description: Optional[str]
    company_meta_keywords: Optional[str]
    company_meta_phones: Optional[str]
    company_meta_emails: Optional[str]
    webhook_event: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "query": "xxx",
                "email_format": "value",
                "person_first_name": "value",
                "person_last_name": "value",
                "person_headline": "value",
                "person_job_title": "value",
                "person_location": "value",
                "person_business_email": "value",
                "person_personal_email": "value",
                "person_company_name": "value",
                "person_city": "value",
                "person_linkedin_id": "value",
                "person_linkedin_url": "value",
                "company_name": "value",
                "company_founded": "value",
                "company_size": "value",
                "company_type": "value",
                "company_country": "value",
                "company_industry": "value",
                "company_address": "value",
                "company_linkedin_url": "value",
                "company_linkedin_id": "value",
                "company_meta_title": "value",
                "company_meta_description": "value",
                "company_meta_keywords": "value",
                "company_meta_phones": "value",
                "company_meta_emails": "value",
                "webhook_event": "new_enrichment_found"
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
