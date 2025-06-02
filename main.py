from fastapi import FastAPI, HTTPException, Query
import json

app = FastAPI()


def load_data():
    with open("patients.json", "r") as file:
        data = json.load(file)
    return data


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/about")
def read_about():
    return {"About": "this is an about page "}


@app.get("/view")
def view_all_data():
    data = load_data()
    return data


@app.get("/view/{patient_id}")
def view_data(patient_id: str):
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="patient not found")


@app.get("/sort")
def sort_patients(
    sort_by: str = Query(
        ..., description="Sort on the basis of weight, height and bmi"
    ),
    order: str = Query("asc", description="Sort in asc or desc order"),
):
    valid_sort_fields = ["weight", "height", "bmi", "age"]

    if sort_by.strip() not in valid_sort_fields:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid field to sort by select from {valid_sort_fields}",
        )

    if order.strip() not in ["asc", "desc"]:
        raise HTTPException(
            status_code=400,
            detail="Invalid field to order by select from ['asc', 'desc']",
        )

    data = load_data()
    sort_order = True if order == "desc" else False
    return sorted(
        data.values(),
        key=lambda x: x[sort_by],
        reverse=sort_order,
    )
