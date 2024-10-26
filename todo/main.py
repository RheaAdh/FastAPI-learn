from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Todo(BaseModel):
    id:int
    title:str
    completed:bool

todos=[]

@app.get("/todos")
def get_todos():
    return todos

@app.get("/todos/{todo_id}")
def get_todo(todo_id:int):
    for todo in todos:
        if todo['id']==todo_id:
            return todo
    return {"error":"Todo not found!"}

@app.post("/todos")
def create_todos(todo: Todo):
    todos.append(todo.dict())
    return todos  

