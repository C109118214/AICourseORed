# -*- coding: utf-8 -*-
def func_1(x):
    n = len(x)
    meanv = sum(x) / n 
    x.append(meanv)
    print("func_1運算結果", x)

def func_2(x):
    result = sum(x) ** 2
    x.append(result)
    print("func_2運算結果", x)
    
sample = [5,8,9,6,4,1,5,3,6,2]
# =============================================================================
# func_1(sample)
# print(sample)
# func_2(sample)
# print(sample)
# =============================================================================
# =============================================================================
# func_2(sample)
# print(sample)
# func_1(sample)
# print(sample)
# =============================================================================

func_1(sample.copy())
print(sample)
func_2(sample.copy())
print(sample)
