# -*- coding: utf-8 -*-
with open('0050.csv', 'r', encoding='utf-8') as file:
    # 使用 readline 逐行讀取
    line = file.readline()
    # 沒有讀取到文字，讀取到最後一行為空字串
    # 就表示結束了，While迴圈也會停止
    while line:
        print(line.strip())  # 去除換行符號並印出每行
        line = file.readline()  # 讀取下一行

