# -*- coding: utf-8 -*-
student_id = int(input("請輸入學號末兩碼："))
total = int(input("請輸入商品金額："))

Num = student_id + total

A = Num % 11

if A == 0:
    print("可以獲得贈品")
else:
    diff = 11 - A
    print(f"還差{diff}元")

