# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 11:29:58 2025

@author: user
"""

shop_name_list = ["M", "K", "B"]
score_list = [60, 85, 90]
price_list = [145, 200, 220]
CP_ratio_list = []

for i in range(len(shop_name_list)):
    CP_ratio = score_list[i] / price_list[i]
    CP_ratio_list.append(CP_ratio)

print(CP_ratio_list)

Max_CP = max(CP_ratio_list)
print(Max_CP)
# 查看CP值最高的索引號是多少
Max_CP_index = CP_ratio_list.index(Max_CP)
print(Max_CP_index)

print("CP值最高的速食店為", shop_name_list[Max_CP_index])