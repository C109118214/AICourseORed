# -*- coding: utf-8 -*-

level = int( input("請輸入菱形要印出幾層 =") )

for i in range(1, level * 2):
    if i <= level:
        blank = "  " * (level - i)
        star = "+ " * (i * 2 - 1)
        
    else:
        blank = "  " * (i - level)
        star = "+ " * ( ( i - 2 * (i - level) ) * 2 - 1 )
        
    print(blank + star)
    