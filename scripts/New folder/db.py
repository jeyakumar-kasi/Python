# -*- coding: utf-8 -*-
"""
Created on Fri May 19 10:25:44 2023

@author: JeyakumarKasi
"""

from sqlalchemy import create_engine

cock_user = 'staguser'
cock_password = 'Dignifying-Gooseberries'
cock_host = 'stg-roach.do.mpkkt.net'
cock_port = 26257
cock_db = 'mpokket'

roach_engine = None


def connect():
    global roach_engine
    if roach_engine is None:
        cockroachdb_uri = f"cockroachdb://{cock_user}:{cock_password}@{cock_host}:{cock_port}/{cock_db}?sslmode=prefer"
        # print(f"Connecting to {cockroachdb_uri} ...")

        connect_args = {"application_name": 'mpokket'}
        roach_engine = create_engine(cockroachdb_uri, connect_args=connect_args, pool_size=10, max_overflow=20, pool_pre_ping=True, pool_recycle=85)
        # print(roach_engine)
    return roach_engine


def execute(query, params=None):
    # print("[SQL] ", end="")
    # if params is None:
    #     print(query)
    # else:
    #     print(query.replace("%s", "'%s'") % (*params, ))
    return connect().execute(query, params)
