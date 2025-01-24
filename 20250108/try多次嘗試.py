# -*- coding: utf-8 -*-
def sumnfunc(n):
    sumi = 0
    for i in range(1, n + 1):
        sumi+= i
    return sumi

try_times = 0 #嘗試的次數
# 最多嘗試五次
while try_times < 5:
    try:
        num = int(input("請輸入正整數："))
        result = sumnfunc(num)
        print(result)
        break
    except:
        print("不要輸入奇怪的東西")
        try_times+= 1 # 失敗時，次數加一
