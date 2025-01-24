# ch7-27.py 功能: 貨幣時間價值之現值
def pvfix(fv, i, n):
# fvfix: 計算現值公式 
    return(fv / ((1 + i) ** (n)))
fv = float(input('請輸入存入終值 = '))
rate = float(input('請輸入年利率 = '))
period = int(input('輸入n年前 = '))
print('% d 年前的現值 = %6.2f' % (period, pvfix(fv, rate, period)))