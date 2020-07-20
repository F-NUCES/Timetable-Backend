import database as db
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://timetable.mrafay.me:5000",
    "http://timetable.mrafay.me"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return RedirectResponse("/docs")
    
@app.get("/courses")
async def courses():
    return JSONResponse(db.list_courses())


@app.get("/course")
async def course(name: str):
    return JSONResponse(db.fetch_course(name))  # type: ignore
