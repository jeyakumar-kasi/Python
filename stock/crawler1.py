# -*- coding: utf-8 -*-
"""
Created on Sun Apr 02 18:41 2023

@author: <jeyakumar.kasi@hyproid.com>
"""

import datetime as dt

with open("./run.txt", 'a') as fh:
    fh.write(f"[{str(dt.datetime.now())}] Success. \n")


