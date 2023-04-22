# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 10:52:45 2022

@author: <jeyakumar.k@datafoundry.ai>
"""
# from random import randint
#
# a = [randint(0, 9) for i in range(6)]
# print(a)
# min_no= min(a)
# print(f"Min: {min_no}")
#
# max_no= max(a)
# print(f"Max: {max_no}")
#
#
# mean= sum(a)/len(a)
# print(f"Mean: {mean}")
#
# import numpy as np
# print(np.min(np.array(6)))




# def f(external_user_id):
#     external_user_id = tuple(external_user_id)
#     if len(external_user_id) == 1:
#         # Parse the value
#         external_user_id = str(external_user_id).replace(",", "")
#     q = f"SELECT * FROM IN {external_user_id}"
#     print(q)

# f(["437483743843"])
# f(["437483743843", "7438434834638"])

from uuid import uuid4

def get_random_number(min_digits=29):
    if min_digits > 32:
        message = f'Error: Couldn\'t generate the requested {min_digits} random number. Maximum of 32 chars allowed.'
        print(message)
        raise Exception(message)
    return uuid4().hex[:min_digits]


api_key = get_random_number().upper()
print(api_key)




# for rand_no in range(1, 10):
#     if rand_no % 2 == 0:
#         print("Number is: " + str(rand_no))

# a = [randint(0, 9) for rand_no in range(6)]
# print(a)
# print(max(a))

# import statistics
# m = statistics.mean(a)
# print(m)

# import statistics
# print(sum(a)/len(a))
# print(statistics.mean(a))
# print(np.max(a), np.mean(a))
#

