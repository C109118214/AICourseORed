# -*- coding: utf-8 -*-
# 讓使用者輸入層數
level = int(input("請輸入直角三角形的層數："))

for i in range(1, level + 1):
    # 根據現在是第幾層，輸出幾個*
    for j in range(i):
        # 每個*最後接一個空格，而不是預設的換行
        print("*", end = "")
    print() # 內圈結束，換行