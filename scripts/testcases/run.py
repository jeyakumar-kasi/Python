# -*- coding: utf-8 -*-


# import pymongo
# DB_HOST = 'mongodb://192.168.117.138:27017/?retryWrites=true&serverSelectionTimeoutMS=5000&connectTimeoutMS=10000'
# DB_NAME = 'emp'
# client = pymongo.MongoClient(DB_HOST)
# db = client.get_database(DB_NAME)    

from config.db_connection import database as db
emp_db = db.get_collection('employee')



# def get_db(db_name=None):
#     db_name = db_name or DB_NAME
#     db = client.get_database(db_name)
#     return db


# Schema
from pydantic import BaseModel
from typing import Optional

class Emp(BaseModel):
    id: int
    name: str=None
    email: str=None
    
class Update(BaseModel):
    name: Optional[str]
    email: Optional[str]
    
    
# API
from fastapi import FastAPI
app = FastAPI()




@app.get('/')
def home():
    return {"status": "OK"}


# @app.get('/emp', response_model=Emp)
# async def get():
#     emp_db = get_db().get_collection('employee')
#     return emp_db.find()


@app.get('/emp/{id}', response_model=Emp)
async def get_emp(id: int):
    # emp_db = get_db().get_collection('employee')
    return emp_db.find_one({'id': id})

    
@app.post('/emp')
def create_emp(data: Emp):
    # Make it as Dict
    data = data.dict()
    cursor = emp_db.insert_one(data)
    if cursor.acknowledged:
        return {"message": f"{data.get('name')} - created successfully"}
    return {"message": f"Failed to create {data.get('name')}."}


# @app.put('/emp/{id}')
# def update_emp(id: int, data: Update):
#     emp_db = get_db().get_collection('employee')
#     # Ignore empty values
#     data = {k: v for k, v in data.dict().items() if v is not None}
    
#     cursor = emp_db.update_one({'id': id}, {'$set': data})
#     if cursor.modified_count == 1:
#         return {"message": "Updated successfully"}
#     return {"message": "Failed to update"}


# @app.delete('/emp')
# def delete_emp(id: int):
#     emp_db = get_db().get_collection('employee')
    
#     cursor = emp_db.delete_one({'id': id})
#     if cursor.deleted_count == 1:
#         return {"message": "Deleted successfully"}
#     return {"message": "Failed to Delete."}





    