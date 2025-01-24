Num = int(input("請輸入大於1的正整數 = "))
flag = True
for i in range(2, Num):
    if Num % i == 0:
        print("%d%s%d%s%d"  %(i , " 乘於 " , Num // i , " 是 " , Num ))
        flag = False
        break
if flag == True :
    print("%d 是質數"  %(Num))
else:
    print("%d 不是質數"  %(Num))