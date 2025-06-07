import json


def load_data():
    with open("patients.json", "r") as file:
        data = json.load(file)
    return data


def videw_data(patient_id: str):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    return {"error": "Patient not found"}


# print(videw_data("P005"))


def data():
    data = load_data()
    return data.values()


print(data())
