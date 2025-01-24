# -*- coding: utf-8 -*-
def sumnfunc(n):
    sumn = 0
    
    for i in range(1, n + 1):
        sumn+= i
    
    return sumn

num = int(input("請輸入正整數："))
result = sumnfunc(num)
print(result)

result_2 = sumnfunc(5)
print(result_2)