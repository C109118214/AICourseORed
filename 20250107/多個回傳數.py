# -*- coding: utf-8 -*-

def A(X, Y):
   X = X ** 3
   Y = Y ** 2
   return X, Y

num_1 = 2
num_2 = 3
result_X, result_Y = A(num_1, num_2)
print(result_X, result_Y)

# 有一個以上的回傳值
# 用一個變數定義，就會變成tuple型別
result = A(num_1, num_2)
print(result)
print(result[0])
print(result[1])

#只有兩個回傳值，但有三個變數要定義，就會出錯
result_X, result_Y, result_Z = A(num_1, num_2)