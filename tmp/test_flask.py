# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 10:52:45 2022

@author: <jeyakumar.k@datafoundry.ai>
"""

# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route("/")
# def index():
#     return "All OK"

# if __name__ == "__main__":
#     app.run()#host="0.0.0.0")



partner_info = {
    "partner_name": "Baaji",
    "api_ket_ttl": 0,
    "is_active": True,
    "created_on": "OK",
    "updated_on": "Updted"
}

def parse_data_to_query(data):
    columns_str = ""
    for clm in data.keys():
        columns_str += "`" + clm + "`, "
    columns_str = "(" + columns_str.rstrip(", ") + ")" if columns_str else ""

    values_str = ""
    for value in data.values():
        values_str += "'" + str(value) + "', "
    values_str = "(" + values_str.rstrip(", ") + ")" if values_str else ""
    return columns_str, values_str

# columns_str, values_str = parse_data_to_query(partner_info)
# query = "INSERT INTO tbl_acquisition_partner %s VALUES %s" % (columns_str, values_str)
# print(query)

partner_name = "Credmudra"

s = {"salaried": {"T0": "Salaried_Onb_T0_{partner_name}", "T1": "", "T10": "", "T3": "Salaried_Onb_T3_{partner_name}",
"T7": "Salaried_Ond_T7_{partner_name}"}, "salaried_in_cash": {"T0": "SIC_Onb_T0_{partner_name}", "T1": "", "T10": "",
"T3": "SIC_Onb_T3_{partner_name}", "T7": "SIC_Onb_T7_{partner_name}"}, "student": {"T0": "Student_Onb_T0_{partner_name}",
"T1": "", "T10": "", "T3": "Student_Onb_T3_{partner_name}", "T7": "Student_Onb_T7_{partner_name}"}}

import json
s = json.dumps(s).replace("{partner_name}", partner_name)

print(s)



