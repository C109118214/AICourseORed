# -*- coding: utf-8 -*-
level = int( input("請輸入菱形要印出幾層 =") )

for i in range(1, level + 1):
    output = ""
    for k in range(1, level- i + 1):
        output+= "  "
    
    for k in range(1, i * 2):
        output+= "+ "
       
    print(output)
    
for i in range(level - 1, 0, -1):
    output = ""
    for k in range(1, level - i + 1):
        output+= "  "
    
    for k in range(1, i * 2):
        output+= "+ "
       
    print(output)