def compute(x, y):
    while y:
        x, y = y, x % y
    return x
num = input()
x, y = num.split(",")
x, y = int(x), int(y)
print(compute(x, y))