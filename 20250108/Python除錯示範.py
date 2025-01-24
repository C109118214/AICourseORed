# -*- coding: utf-8 -*-
def sumnfunc(n):
    sumi = 0
    for i in range(1, n + 1):
        sumi+= i
    return sumi
result = sumnfunc(5)
print(result)