M = 0   #累計月數
PV = float(input("請輸入每月存入的本金:"))
MPV = 0   #月存款累計金額（加計利息）
r = float(input("請輸入年利率(%), 1.5代表1.5% = ")) / 100
Target = float(input("請輸入存到第一桶金的目標金額 = "))
while( MPV < Target):
    #每個月存入金額加上之前累計的存款金額乘上利率因子
    MPV = (MPV + PV) * (1 + ( r / 12)) 
    M = M + 1
#累計的月數除以12取商（年）與餘數（月）
[Year, Month] = divmod(M, 12)    
print("每個月存入本金%.2f, 年利率:%.2f%s，共儲存了%d個月"  
      %(PV, r * 100, "%", M))
print("%d年%d月後, 可存到 = %.2f %s"  %(Year, Month, MPV, "元"))