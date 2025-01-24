# -*- coding: utf-8 -*-
import random as rd

# 一番賞抽獎
prize_list = ["D"] * 5 + ["C"] * 3 + ["B"] * 2 + ["A"]
print(prize_list)

Num = int(input("請輸入抽幾次："))
get_prize_list = []
for i in range(Num):
    # 查看獎池裡面還有多少
    prize_len = len(prize_list)
    prize_index = rd.randint(0, prize_len-1)
    prize = prize_list.pop(prize_index)
    print(prize_list)
    print(prize_len , prize_index, prize)
    get_prize_list.append(prize)
print(get_prize_list)