import database as db
from fastapi import FastAPI
from fastapi.responses import JSONResponse


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/courses")
async def courses():
    return JSONResponse(db.list_courses())


@app.get("/course")
async def course(name: str):
    return JSONResponse(db.fetch_course(name))  # type: ignore
