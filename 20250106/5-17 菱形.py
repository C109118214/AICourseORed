# -*- coding: utf-8 -*-
level = int( input("請輸入菱形要印出幾層 =") )
for i in range(level):
    for j in range(level - i - 1):
        print(" ", end = " ")
    for k in range((2 * i) + 1):
        print("+", end = " ")
    print()

# 程式與上一段相同，僅更改range的內容
for i in range(level - 2, -1, -1):
    for j in range(level - i - 1):
        print(" ", end = " ")
    for k in range((2 * i) + 1):
        print("+", end = " ")
    print()
