# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 22:29:23 2023

@author: JeyakumarKasi
"""

from pymongo import MongoClient


MONGODB_URL = 'mongodb://192.168.117.138:27017/?retryWrites=true&serverSelectionTimeoutMS=5000&connectTimeoutMS=10000'

# connection to docDB
mongoClient = MongoClient(MONGODB_URL)

ENV_NAME = 'TEST'
DB_NAME = 'test_emp' if ENV_NAME == 'TEST' else 'emp'
# getting database from the cluster
database = mongoClient[DB_NAME]
