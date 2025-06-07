from pydantic import BaseModel, EmailStr, AnyHttpUrl
from typing import List, Dict, Optional


class Patient(BaseModel):
    name: str
    email: EmailStr
    linkedin_url: AnyHttpUrl
    age: int
    weight: float
    married: bool
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]


def insert_patient(patient: Patient):
    print("Patient Name: ", patient.name)
    print("Email: ", patient.email)
    print("Linkedin: ", patient.linkedin_url)
    print("Age: ", patient.age)
    print("Weight: ", patient.weight)
    print("Married: ", patient.married)
    print("Allergies: ", patient.allergies)
    print("Contact details: ", patient.contact_details)

    print("success")


patient_info = {
    "name": "shivam",
    "age": 20,
    "weight": 45.5,
    "married": False,
    "contact_details": {"email": "shivam@yahoo.com"},
    "allergies": ["shellfish"],
    "email": "shiv@amgmail.com",
    "linkedin_url": "https://linkedin.com/in/shivambhardwaj03/",
}

patient_one = Patient(**patient_info)

insert_patient(patient_one)
