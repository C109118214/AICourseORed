# TODO
num = int(input())

total = 0 # 累加的變數
# 從0開始到num為止，將5, 10, 15...累加起來
for i in range(0, num + 1, 5):
    total += i
print(total)