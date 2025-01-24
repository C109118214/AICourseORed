# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 10:23:53 2025

@author: user
"""

list_1 = [1, 1, 2, 3]

list_1.append(4)
print(list_1)

list_2 = [5,6,7]
#list_1.append(list_2)
list_1.extend(list_2)
print(list_1)

list_1.insert(1, 999)
print(list_1)

# 將指定的元素從串列中刪除，會刪除找到的第一個符合的元素
list_1.remove(1)
print(list_1)

print( list_1.pop() )
print(list_1)

print( list_1.pop(1) )
print(list_1)

list_1.sort()
print(list_1)

list_1.sort(reverse = True)
print(list_1)

list_1.clear()
print(list_1)
