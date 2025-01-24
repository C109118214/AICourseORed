level = int(input("請輸入直角三角形要印出幾層 = "))
for i in range(1, level + 1): 
    for j in range(i):
        print("*", end = " ") 
    print( )