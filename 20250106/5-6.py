# -*- coding: utf-8 -*-
import random as rd

Num = int(input("請問要投幾次骰子："))
Dict = [0] * 6 # 記錄各個點數出現的次數
for i in range(Num):
    index = rd.randint(1, 6)
    Dict[index - 1] += 1
    print("骰到", index)
    print(Dict)

print(Dict)
for i in range(len(Dict)):
    print("%d點出現了%d次，出現機率為%.2f" % (i+1, Dict[i], Dict[i] / Num))