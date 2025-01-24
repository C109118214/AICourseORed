# TODO
num = int(input())

# 架設做3次，i不會用到
for i in range(num):
    digits = int(input()) # 讓使用者輸入整數
    d = digits # 複製一份輸入的digits，因為輸出會用到原始的digits
    total = 0 # 累加所有的位數的和
    # 數字還大於10位數，就繼續進行
    while d != 0: 
        total+= d % 10 # 取數字的個位數，加到total
        d = d // 10 # 將加過的個位數，用整數除法去除
    print(f"Sum of all digits of {digits} is {total}")

    



"""
Sum of all digits of _ is _
"""