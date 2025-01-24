# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 16:13:17 2025

@author: user
"""

Years = int(input("請輸入西元年："))

if (Years % 400 == 0) or (Years % 4 == 0 and Years % 100 != 0):
    print(f"{Years}年為閏年")
else:
    print(f"{Years}年為平年")