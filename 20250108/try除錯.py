# -*- coding: utf-8 -*-
def sumnfunc(n):
    sumi = 0
    for i in range(1, n + 1):
        sumi+= i
    return sumi
try:
    num = int(input("請輸入正整數："))
    result = sumnfunc(num)
    print(result)
except:
    print("不要輸入奇怪的東西")
