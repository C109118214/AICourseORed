# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 15:06:11 2025

@author: user
"""

hours = int(input("請輸入借用了幾小時："))
mins = int(input("請輸入借用了幾分鐘："))

if mins > 0 and mins <= 30:
    hours+= 0.5
elif mins > 30:
    hours+= 1
    
range_1 = 4 * 2 * 10
range_2 = (8 - 4) * 2 * 20

if hours <= 4:
    result = 10 * 2 * hours
elif hours <= 8:
    result = range_1 + (hours - 4) * 20 * 2
else:
    result = range_1 + range_2 + (hours - 8) * 40 * 2
    
print(f"總共{result}元")