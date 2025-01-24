# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 10:11:49 2025

@author: user
"""

f_list = [1, 1]
n=10
# 因為原本就已經有1,1了，跳過兩個數字
# i沒有參與運算，這個範例只是要定義"做幾次"
# range(10 - 2)等同於range(8)
# i從0開始到7總共八個數字(八次)
for i in range(n-2):
    # 抓取list最後一個與倒數第二個數字來加總
    num = f_list[-1] + f_list[-2]
    f_list.append(num)
    print(num, f_list)
