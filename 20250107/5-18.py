# -*- coding: utf-8 -*-
Num = int(input("請輸入正整數："))

flag = True # 假設輸入的值是質數

for i in range(2, Num):
    # 若2到Num-1之間有數字可以整除Num
    # 就不是質數
    if Num % i == 0:
        flag = False # 標註不是質數
        break # 結束迴圈

# 直到最後，若Flag維持True，那這個數字就是質數
# 反之，則不是質數
if flag:
    print(f"{Num}是質數")
else:
    print(f"{Num}不是質數")
