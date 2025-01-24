# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 11:16:38 2025

@author: user
"""

list_1 = [1, 1, 2, 3]
list_1.append(4)
print(list_1)

#pop_num = list_1.pop()
#print(pop_num)
list_1.pop()
print(list_1)

a = 1
print(id(a))
a + 1
print(id(a))
print(a)

count = 0
for i in range(1,5):
    count += 1
    # count = count + 1
    print(count, id(count))

