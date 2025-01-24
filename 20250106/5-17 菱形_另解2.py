# -*- coding: utf-8 -*-
level = int( input("請輸入菱形要印出幾層 =") )

for i in range(1, level + 1):
    blank = "  " * (level - i)
    star = "+ " * (i * 2 - 1)
       
    print(blank + star)
    
for i in range(level - 1, 0, -1):
    blank = "  " * (level - i)
    star = "+ " * (i * 2 - 1)
       
    print(blank + star)