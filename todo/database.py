import os

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from dotenv import load_dotenv
load_dotenv()

DATABASE_URL = "mysql+mysqlconnector://root:"+os.getenv("DB_PASSWORD")+"@localhost:3306/todo"

engine = create_engine(DATABASE_URL)
metadata = MetaData()
Sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
BaseModel = declarative_base()
