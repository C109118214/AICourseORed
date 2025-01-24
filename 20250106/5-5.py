# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 10:45:26 2025

@author: user
"""

Temp_str = list( input("請輸入一字串：") )
print(Temp_str)
N = len(Temp_str)
# 走訪字串
for i in range(N):
    print(Temp_str[i])
    
print("----------")
# 反向走訪
for i in range(N-1, -1, -1):
    print(Temp_str[i], end = "")
    
