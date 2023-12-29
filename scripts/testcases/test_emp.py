# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 13:52:03 2023

@author: JeyakumarKasi
"""

import json
# from fastapi.testclient import TestClient

from run import app


# # Create the TestClient Instance
# client = TestClient(app)

def test_home(test_client):
    res = test_client.get('/')
    
    assert res.status_code == 200
    assert res.json()['status'] == 'OK'
    

# def test_create_emp(mongo_mock):
def test_create_emp(test_client):
    data = {
        "id": 1,
        "name": "test_name",
        "email": "test_email@gmail.com"
    }
    res = test_client.post('/emp', data=json.dumps(data))
    
    assert res.status_code == 200
    assert res.json()["message"] == f"{data.get('name')} - created successfully"


# def test_get_emp(mongo_mock):
def test_get_emp(test_client):    
    res = test_client.get('/emp/1')
    
    assert res.status_code == 200
    assert res.json()["id"] == 1
    assert res.json()["name"] == "test_name"
    assert res.json()["email"] == "test_email@gmail.com"
    
    
    

    
