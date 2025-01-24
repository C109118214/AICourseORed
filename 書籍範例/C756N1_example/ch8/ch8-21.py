# ch8-21: 定義貨幣時間價值的類別
class timevalue:
    # 終值    
    def fvfix(self, pv, i, n):
        # fvfix: 計算終值公式    
        fv = pv * (1 + i) ** n
        return(fv)
    # 現值
    def pvfix(self, fv, i, n):
        # pvfix: 計算現值公式    
        pv = fv / ((1 + i) ** n)
        return(pv)
# 設定初始值
pv = int(input('存入現值(100) = '))  # 可以輸入100
fv = float(input('存入終值(115.93) = '))  # 可以輸入115.93
i = float(input('年利率(0.03) = '))  # 可以輸入0.03
n = int(input('請輸入期數(5) = '))  # 可以輸入5    
# 呼叫TimeValue類別，建構物實體
tv1 = timevalue( )
# 呼叫物件實體的方法
print('%d年後的終值 = %10.2f' %(n, tv1.fvfix(pv, i, n)))
print('%d年後的現值 = %10.2f' %(n, tv1.pvfix(fv, i, n)))