# TODO
num = int(input())

total = 0
# i 代表的是N-1，所以到num -1 就能計算完N-1跟N的部分
for i in range(1, num):
    total += 1 / (i ** 0.5 + (i + 1) ** 0.5 )
    
print(f"{total:.4f}")