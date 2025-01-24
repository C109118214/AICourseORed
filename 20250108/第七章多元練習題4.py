# -*- coding: utf-8 -*-
import datetime

def check(n):
    flag = True # 假設輸入的值是質數
    for i in range(2, n):
        # 若2到Num-1之間有數字可以整除Num
        # 就不是質數
        if n % i == 0:
            flag = False # 標註不是質數
            break # 結束迴圈
    # 直到最後，若Flag維持True，那這個數字就是質數
    # 直接回傳這個結果
    return flag
    
Num_range = int(input("請輸入正整數："))
start_time = datetime.datetime.now()

result_list = [] # 儲存結果
# 驗證2到Num_range之間的質數
for Num in range(2, Num_range + 1):
    result = check(Num)
    if result:
        print(Num, end = " ")
    

end_time = datetime.datetime.now()

print(end_time - start_time)