# ch7-28.py 功能: 普通年金現值之教育基金
def PVOA(PMT, i, n):
# PVOA: 計算普通年金現值公式 
    PVIFA = 0
    # 計算年金現值複利因子
    for t in range(1, n + 1):
        PVIFA = PVIFA + ((1 + i) ** (-t))
    return(PMT * PVIFA)
cash = int(input('請輸入原始投資金額 = '))
PMT = int(input('請輸入每年領回金額 = '))
i = float(input('請輸入年利率 = '))
n = int(input('請輸入可以領回總年數 = '))
invest = round(PVOA(PMT, i, n) , 2)
print('本教育基金之投資方案現值 = ', invest)
print('% s % d % s % d % s % d ' % ('投資現值', invest, ' - 原始金額', cash, ' = ', invest - cash))
if(invest - cash) < 0:
    print('負報酬, 不建議購買')
else:
    print('正報酬, 建議購買')