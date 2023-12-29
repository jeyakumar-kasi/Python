# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 00:32:30 2023

@author: JeyakumarKasi
"""

from flask import Flask

app = Flask(__name__)

@app.route('/v1/underwriter/bre', methods=['POST'])
def bre_details():
    bre_details = {
        "color": "AMBER",
        "msg": "success",
        "probability": 0.89,
        "status": "success"
    }
    return bre_details

if __name__ == '__main__':
    app.run('0.0.0.0', port=8888, debug=True)
    