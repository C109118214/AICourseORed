# -*- coding: utf-8 -*-
# 讓使用者輸入層數
level = int(input("請輸入直角三角形的層數："))

# i代表層數
for i in range(level):
    # 那一層前面需要輸出幾個空格
    for j in range(level - i - 1):
        print(" ", end = " ")
        
    # 根據現在是第幾層，輸出幾個+
    for k in range(i*2 + 1):
        # 每個+最後接一個空格，而不是預設的換行
        print("+", end = " ")
    print() # 內圈結束，換行
