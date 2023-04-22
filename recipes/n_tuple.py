# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 10:52:45 2022

@author: <jeyakumar.k@datafoundry.ai>
"""

# Unpacking
t = ('Y', 'A', 'B', 'X', 'you', ('abc', 'xyz'), 'c')

try:
    y, a, *b, x = t
    print(y, a, b)
    print(y, a, b, x)
except ValueError:
    print("values are not matched")



