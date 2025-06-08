import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, computed_field
from fastapi.responses import JSONResponse

app = FastAPI()


def save_data(data):
    with open("patients.json", "w") as file:
        json.dump(data, file)


def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
        return data


class Patient(BaseModel):

    id: str = Field(..., description="ID of the patient", examples=["P001"])
    name: str = Field(..., description="Patient name")
    city: str = Field(..., description="Patient city name")
    age: int = Field(..., gt=0, lt=120, description="Height in meters")
    gender: str
    height: float = Field(..., description="Height in meters")
    weight: float = Field(..., description="Weight in kilograms")

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight / (self.height**2), 2)
        return bmi

    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "UnderWeight"
        elif self.bmi < 25:
            return "Normal"
        elif self.bmi < 30:
            return "OverWeight"
        else:
            return "Obese"


@app.post("/")
def greetings():
    return {"message": "hello world"}


@app.post("/create")
def create_patient(patient: Patient):

    # load data
    data = load_data()

    # check pre exsiting
    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient Already Exists")

    # save patient
    data[patient.id] = patient.model_dump(exclude=["id"])

    save_data(data)

    return JSONResponse(status_code=201, content={"message": "success create"})
