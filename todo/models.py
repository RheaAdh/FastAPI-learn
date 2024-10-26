from sqlalchemy import Column,Integer,String,Boolean
from database import BaseModel

class TodoModel(BaseModel):
    __tablename__='todos'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)  # Specify a length for VARCHAR
    completed = Column(Boolean, default=False)