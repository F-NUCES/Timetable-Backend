import database as db
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/courses")
async def courses():
    return db.list_courses()


@app.get("/course")
async def course(name: str):
    return db.fetch_course(name)  # type: ignore
