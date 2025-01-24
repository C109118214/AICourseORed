# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 09:44:10 2025

@author: user
"""
# 預設從右往左處理，
# A先處理右邊的True and False = False
# 再處理中段的False and False = False and (True and False) = False
# 最後處理True or False = True or (False and True and False) = True
A = True or False and True and False
B = (True or False) and (True and False)

print(A)
print(B)

