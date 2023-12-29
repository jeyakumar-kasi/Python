# -*- coding: utf-8 -*-5
"""
Created on Fri Nov 18 10:52:45 2022

@author: <jeyakumar.k@datafoundry.ai>
"""

def login(a, b):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            print("Before decorator")
            print("The value", a, b)
            fn(*args, **kwargs)
            print("After decorator")
            return fn
        return wrapper
    return decorator

@login(a=10, b="Welcome")
def hello():
    print("Hello function.")

# hello()

from abc import ABC, abstractmethod

class MyAbstract(ABC):
    @abstractmethod
    def no_of_tyres(self):
        pass

class Bus(MyAbstract):
    def no_of_tyre(self):
        self.no_of_tyre = 10


class Car(MyAbstract):
    def no_of_tyre(self):
        self.no_of_tyre = 4

    def no(self):
        self.no_of_tyres = 4


c = Car()
c.no_of_tyre()
print(c.no_of_tyre)




class A:
    def __init__(self):
        self.price = 0
        print("A class")

    @classmethod
    def fixed_price(clss):
        clss.price = 100

    @staticmethod
    def is_price_ok(price):
        return price < 50

    def my_price(self):
        self.price = 10

    def show(self):
        print("A class function")
        print("Price: ", self.price)

class B(A):
    def __init__(self):
        print("B class")

    def show(self):
        print("B class function")

class D(B):
    def __init__(self):
        print("D class")

    def show(self):
        print("D class function")


class C(D):
    def show(self):
        super().show()
        super(D, self).show()
        super(B, self).show()
        print("C class function")


if __name__ == "__main__":
    # c = C()
    # c.show()
    # B.show(c)

    # a = A()
    # a.my_price()
    # print(a.price)
    # print("Price is OK " if A.is_price_ok(a.price) else "Price is too much.")
    #
    # A.fixed_price()
    # print(A.price)


    d = [{
        "name": "jai",
        "age":"24",
        "addr": "Indra nagar",
        "zip": "84323299"
    }, {
        "name": "Jan",
        "age":"40",
        "addr": "Indra nagar",
        "zip": "84323299"
    },
        {
            "name": "BBBan",
            "age":"4",
            "addr": "Indra nagar",
            "zip": "84323299"
        }
    ]

    # dd = sorted(d.items(), key=lambda (k,v): (v,k))
    try:
        dd = sorted(d, key=lambda x: int(x["age"]), reverse=True)
        # raise Exception("EROROR idsdsdjs")
        # dd[0]["fdfhdf"]
    except KeyError:
        print("Key Ettotttt")
    except Exception as e:
        print("Error", str(e))
    else:
        print(dd)

# Python Program to depict multiple inheritance
# when every class defines the same method

# class Class1:
#     def m(self):
#         print("In Class1")
#
# class Class2(Class1):
#     def m(self):
#         print("In Class2")
#
# class Class3(Class1):
#     def m(self):
#         print("In Class3")
#
# class Class4(Class2, Class3):
#     def m(self):
#         print("In Class4")
#
# obj = Class4()
# obj.m()
#
# Class2.m()
# Class3.m(obj)
# Class1.m(obj)




