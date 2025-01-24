# ch7-25.py 功能: 貨幣時間價值之終值
def fvfix(pv, i, n):
# fvfix: 計算終值公式
    return(pv * (1 + i) ** n)
cash = int(input('請輸入存入現值 = '))
rate = float(input('請輸入年利率 = '))
period = int(input('請輸入存款年數 = '))
print('%d年後的本利和 = %6.2f' %(period, fvfix(cash, rate, period)))