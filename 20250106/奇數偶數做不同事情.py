# -*- coding: utf-8 -*-
for i in range(1, 11):
    if i % 2 != 0:
        print(i, "是奇數")
    else:
        print(i, "是偶數")

for i in range(1, 11):
    reminder = i % 3
    if reminder == 0:
        print("第", i, "天騎腳踏車")
    elif reminder == 1:
        print("第", i, "天跳繩")
    else:
        print("第", i, "天慢跑")