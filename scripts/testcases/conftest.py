# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 21:56:58 2023

@author: JeyakumarKasi
"""

from pytest import fixture
from starlette.config import environ
from starlette.testclient import TestClient
from config.db_connection import database #, X_collection, Y_collection, Z_collection


@fixture(scope="session")
def test_X():
    return {
        "id": "10",
        "name": "test_name",
        "email": "test_email@gmail.com"
    }

# //test_Y and test_Z fixtures should be like test_X


@fixture(scope="session", autouse=True)
def test_client(test_X): #, test_Y, test_Z):
    import run
    application = run.app
    with TestClient(application) as test_client:
        yield test_client

    db = database
    print('DATABASE', db)
    # //Here, delete any objects you have created for your tests
    # db['employee'].delete_one({"id": test_X["id"]})
    #db[Y_collection].delete_one({"_id": test_Y["_id"]})
    #db[Z_collection].delete_one({"_id": test_Z["_id"]})


environ['TESTING'] = 'TRUE'

