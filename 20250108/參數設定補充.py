# -*- coding: utf-8 -*-
def func_1(x, y, *z):
    print(z)
    result = x + y + sum(z)
    return result

a, b, c, d, e = 1, 2, 3, 4, 5

print(func_1(a, b, c, d, e))

# 預設參數，預設參數一定要在位置參數之後
def func_2(score_1, score_2, score_3 = 50):
    print(score_3)
    result = (score_1 + score_2 + score_3) / 3
    return result

print(func_2(80, 80, 80))
print(func_2(80, 80))
print(func_2(score_1 = 50, score_3 = 70, score_2 = 60))
print(12,31)
print(12,34, sep = "/")
print("這是預設", sep = " ", end = "\n")
# =============================================================================
# # 預設參數，預設參數一定要在位置參數之後
# def func_2(score_3 = 50, score_1, score_2 ):
#     print(score_3)
#     result = (score_1 + score_2 + score_3) / 3
#     return result
# 
# print(func_2(80, 80, 80))
# print(func_2(80, 80))
# =============================================================================
