# ch7-26.py 功能: 計算退休金
def FVOA(PMT, i, n):
# FVOA: 計算普通年金終值公式
    FVIFA = 0
    # 計算年金終值複利因子
    for t in range(1, n + 1):
        FVIFA = FVIFA + ((1 + i) ** (n - t))
    print('FVIFA = ', round(FVIFA, 2))
    # 計算退休金 = 年金乘上複利因子 
    return(PMT * FVIFA)
PMT = int(input('輸入每個月存入金額 = '))
rate = float(input('輸入年利率 = '))
period = int(input('輸入預計幾年後退休 = '))
print('% d 年後的退休金終值 = %10.2f' % (period, FVOA(PMT, rate / 12, period * 12)))