# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 14:43:21 2025

@author: user
"""

dict_1 = {"id" : 1}
dict_2 = dict_1

dict_1["name"] = "Winston"
print(dict_2)

print("---------")
dict_1 = {"id" : 1}
dict_2 = dict_1.copy()

dict_1["name"] = "Winston"
print(dict_2)