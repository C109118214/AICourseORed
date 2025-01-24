# -*- coding: utf-8 -*-
lamret = lambda x : x ** 2
print(lamret (6))

# =============================================================================
# def lamret(x):
#     return x ** 2
# =============================================================================
# 可以將lambda函數放入list中，不用幫函數取名
list_1 = [lambda x : x ** 2, 
        lambda x : x ** 3,
        lambda x : x ** 4]
print(list_1[0](6))
print(list_1[1](6))