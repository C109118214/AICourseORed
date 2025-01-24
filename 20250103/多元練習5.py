# -*- coding: utf-8 -*-

Num_1 = int( input("請輸入數值1：") )
Num_2 = int( input("請輸入數值2：") )
Num_3 = int( input("請輸入數值3：") )

list_1 = [Num_1, Num_2, Num_3]
max_num = max(list_1)
min_num = min(list_1)
print(f"最大值為{max_num}")
print(f"最小值為{min_num}")