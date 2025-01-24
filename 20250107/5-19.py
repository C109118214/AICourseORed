# -*- coding: utf-8 -*-
import random as rd

Bingo = rd.randint(1, 20) # 隨機產生1到20的答案

while True:
    Num = int(input("請輸入1到20的數字："))
    if Num == Bingo:
        print("Bingo，恭喜答對!")
        break # 答對就結束迴圈
    elif Num > Bingo:
        print("太大了，猜小一點")
    else:
        print("太小了，猜大一點")
    