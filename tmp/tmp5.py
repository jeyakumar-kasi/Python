# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 01:42:23 2023

@author: JeyakumarKasi
"""

import json

d = '''{
  "color": "AMBER",
  "msg": "success",
  "probability": 0.89,
  "status": "success"
}'''

print(type(json.loads(d)))