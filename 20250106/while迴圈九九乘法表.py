# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 15:53:51 2025

@author: user
"""
i = 1
while i <= 9:
    j = 1
    while j <=9:
        print("%d*%d=%2d" % (i, j, i*j), end = " ")
        j+= 1
    i+= 1
    print()
    