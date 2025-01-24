C = [1000, 900, 700]    #成本
R = [1090, 945, 840]    #預期效益
P = ["A", "B", "C"]     #方案名稱
rate = 0.1    #市場利率
MEI = [ ] 
for i in range(len(C)):
    MEI.append((R[i] / C[i]) - 1 )   #第i筆預期效益除以成本減1新增到串列
#印出標題
print("%8s%10s%10s%10s%10s"  
       %("方案","成本", "收益", "MEI(%)", "是否值得投資"))
#印出結果
for i in range(len(C)):
    if MEI[i] > rate:    #逐筆判斷MEI是否大於市場利率
        msg = "是"
    else: 
        msg = "否"
    print("%8s%13d%12d%9.2f%10s"  
            %(P[i], C[i], R[i], round(MEI[i]*100, 2), msg))