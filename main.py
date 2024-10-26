from fastapi import FastAPI 
from pydantic import BaseModel
app = FastAPI()

class Custom(BaseModel):
    name:str
    age:int

@app.get("/ping")
async def root():
    return {"message": "hey there, this is Rhea!"}

@app.get("/")
async def root():
    return {"message": "hey there please use /ping or /blogs/blogid"}

@app.get("/blogs/comments")
async def read_blog_comments():
    return{"comments":"No comments"}

@app.get("/blogs/{blog_id}")
async def read_blog(blog_id:int,request_body:Custom, q:str=None, name:str=''):
    print(request_body)
    return{"blog_id":blog_id, "name": request_body.name,"age":request_body.age}

# Order matters this will fail 
# @app.get("/blogs/comments")
# async def read_blog_comments():
#     return{"comments":"comment"}




# Steps:
# pip3 install fastapi
# pip3 install uvicorn
# pip3 install pydantic
# uvicorn main:app --reload
# http://127.0.0.1:8000
# http://localhost:8000/docs