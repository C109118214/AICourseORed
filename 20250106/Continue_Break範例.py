# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 16:15:03 2025

@author: user
"""

for i in range(1,21):
    if i % 3 == 0:
        continue
    print(i)
    
print("--------")
for i in range(1,21):
    if i % 3 == 0:
        break
    print(i)
    