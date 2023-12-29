# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 14:00:56 2023

@author: JeyakumarKasi
"""

import pytest
import mongomock

import run
from run import Emp

DB_NAME = 'emp'
emp_col = 'employee'

@pytest.fixture()
def mongo_mock(monkeypatch):
    client = mongomock.MongoClient()
    db = client.get_database(DB_NAME)
    col = db.get_collection(emp_col)    
    
    data: Emp = {
        "id": 1,
        "name": "test_name",
        "email": "test_email@gmail.com"
    }
    col.insert_one(data)
    
    def get_test_db():
        print("Using TEST DB....")
        return db
    
    # Re-assign the 'db'
    monkeypatch.setattr('run.get_db', get_test_db)