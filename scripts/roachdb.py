# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 10:52:45 2022

@author: <jeyakumar.k@datafoundry.ai>
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
        print(f"Connecting to {cockroachdb_uri} ...")

        connect_args = {"application_name": 'mpokket'}
        roach_engine = create_engine(cockroachdb_uri, connect_args=connect_args, pool_size=10, max_overflow=20, pool_pre_ping=True, pool_recycle=85)
    return roach_engine


def execute(query, params=None):
    print("[SQL] ", end="")
    if params is None:
        print(query)
    else:
        print(query.replace("%s", "'%s'") % (*params, ))
    return connect().execute(query, params)

import re
def get_var_name(name):
    return re.sub("[\s]+", "_", re.search("[\w\s]+", name.strip())[0]).lower()

tbl_name = 'public.tbl_acquisition_partner'
q = f"SELECT partner_name FROM {tbl_name}"
res = execute(q).fetchall()

for row in res:
    partner_name = row["partner_name"]
    # print(f"{partner_name:.<30} {get_var_name(partner_name)}")

    q = f"UPDATE {tbl_name} SET partner_slug_name=%s WHERE partner_name=%s;"
    execute(q, params=(get_var_name(partner_name), partner_name))

# Display
q = f"SELECT partner_name, partner_slug_name FROM {tbl_name}"
res = execute(q).fetchall()
for row in res:
    partner_name = row["partner_name"]
    partner_slug_name = row["partner_slug_name"]
    print(f"{partner_name:.<30} {partner_slug_name}")





print(roach_engine)