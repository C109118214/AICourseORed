level = int(input("請輸入等腰三角形要印出幾層 = "))
for i in range(level): 
    for j in range(level - i - 1):
        print(" ", end = " ")
    for k in range((2 * i) + 1):
        print("+", end = " ")
    print( )