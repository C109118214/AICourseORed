# -*- coding: utf-8 -*-
import datetime

Num_range = int(input("請輸入正整數："))
start_time = datetime.datetime.now()

result_list = [] # 儲存結果
# 驗證2到Num_range之間的質數
for Num in range(2, Num_range + 1):
    flag = True # 假設輸入的值是質數
    
    for i in range(2, Num):
        # 若2到Num-1之間有數字可以整除Num
        # 就不是質數
        if Num % i == 0:
            flag = False # 標註不是質數
            break # 結束迴圈
    
    # 直到最後，若Flag維持True，那這個數字就是質數
    if flag:
        result_list.append(Num)
print(result_list)
end_time = datetime.datetime.now()

print(end_time - start_time)