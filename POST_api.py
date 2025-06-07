from fastapi import FastAPI

app = FastAPI()


@app.post("/")
def greetings():
    return {"message": "hello world"}
