from fastapi import FastAPI 
from pydantic import BaseModel

app = FastAPI()

@app.get("/test")
async def root():
    return {"message": "hey there, this is Rhea!"}