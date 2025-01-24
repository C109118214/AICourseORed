# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 10:26:11 2025

@author: user
"""

factor = []

for i in range(1, 101):
    if (i % 5 == 0) and (i % 7 == 0):
        factor.append(i)
        
print("1到100能被5和7同時整除的數字", factor)
print("1到100能被5和7同時整除的數字有幾個", len(factor))
print("1到100能被5和7同時整除的數字加總", sum(factor))

