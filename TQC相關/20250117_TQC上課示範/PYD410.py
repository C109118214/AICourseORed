# TODO
num = int(input()) # 層數

for i in range(1, num + 1):
    space = " " * (num - i) # 第n層有n-1個空格
    star = "*" * (2 * i - 1) # 第n層有2n-1個*
    print( space + star ) # 將空格與星號串接輸出
