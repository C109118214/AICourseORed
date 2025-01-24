# -*- coding: utf-8 -*-
n = int( input("請輸入正整數：") )

sum_1 = 0 # 儲存奇數和
sum_2 = 0 # 儲存偶數和
# 走訪1到n
for i in range(1, n+1):
    # 判斷i是奇數還是偶數
    if i % 2 != 0:
        sum_1+= i
    else:
        sum_2+= i

print(f"1到{n}的奇數和為：{sum_1}")
print(f"2到{n}的偶數和為：{sum_2}")
