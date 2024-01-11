# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 12:03:34 2024

@author: Jeyak
"""

class A:
    def __init__(self, name=None):
        print("Parent (A): ", name)
        
class B:
    def __init__(self, name=None):
        print("Parent (B): ", name)

class C(A, B):
    def __init__(self, name=None):
        super(C, self).__init__(name)
        

C("JK")