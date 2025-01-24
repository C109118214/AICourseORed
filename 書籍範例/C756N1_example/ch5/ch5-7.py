BinV = [0, 1, 1, 0, 1]
DecV = 0
j = len(BinV) - 1    #設定j為2的次方
for i in range(len(BinV)):
    #取出BinV第i個字元乘2的j次方
    DecV = DecV + (BinV[i] * (2 ** j))  
    j -= 1    #j逐圈減1 
print("二進位轉十進位 = ", DecV)