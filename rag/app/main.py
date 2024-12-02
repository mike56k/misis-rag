from fastapi import FastAPI
from app.populate_database import populate_database
from app.query_data import query_rag
from pydantic import BaseModel
from app.parser import crawl


class QuestionRequest(BaseModel):
    question: str


app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Data processor"}


@app.get("/fill_database")
async def fill_database():
    crawl("http://misis.ru")

    populate_database()

    return "Populated"


@app.post("/generate_response")
async def generate_response(request: QuestionRequest):
    result = query_rag(request.question)
    return {"result": result}
