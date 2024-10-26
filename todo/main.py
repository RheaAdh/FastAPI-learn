from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from database import Sessionlocal, engine
from models import TodoModel
from sqlalchemy.orm import Session
from typing import List

app = FastAPI()

# Create database tables
TodoModel.metadata.create_all(bind=engine)

class TodoBase(BaseModel):
    title: str
    completed: bool = False

class TodoResponse(TodoBase):
    id: int
    class Config:
        orm_mode = True

# Dependency to get database session
def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/todos", response_model=List[TodoResponse])
def get_todos(db: Session = Depends(get_db)):
    todos = db.query(TodoModel).all()
    return todos

@app.get("/todos/{todo_id}", response_model=TodoResponse)
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(TodoModel).filter(TodoModel.id == todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found!")
    return todo.first()


@app.delete("/todos/{todo_id}", response_model=TodoResponse)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(TodoModel).filter(TodoModel.id == todo_id)
    db.delete(todo)
    db.commit()
    return todo[-1]
    

@app.post("/todos", response_model=TodoResponse)
def create_todo(todo: TodoBase, db: Session = Depends(get_db)):
    new_todo = TodoModel(title=todo.title,completed=todo.completed)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

# pip3 install -r requirements.txt