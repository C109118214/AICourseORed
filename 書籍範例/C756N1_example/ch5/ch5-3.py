N = int(input("請輸入正整數N = "))   #鍵盤輸入正整數N
sumi = 1 
for i in range(1, N + 1):
    sumi *= i    #將sumi與i相乘後累加給sumi
    print("1 ~ %d 之階乘 = %d" %(i, sumi))   #印出第i層(圈)的階乘值sumi