# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 13:55:54 2024

@author: user
"""

a = 3
print(id(a))
a = a + 1
print(id(a))

list_1 = [1,2,3]
print(list_1)
print(id(list_1))
list_1.append(4)
print(list_1)
print(id(list_1))