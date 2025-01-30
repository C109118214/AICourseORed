# TODO
num = int(input())

total = 0
for i in range(1, num):
    total += 1 / (i ** 0.5 + (i+1) ** 0.5)
print(f"{total:.4f}")