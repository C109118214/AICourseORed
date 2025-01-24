# ch7-18.py功能: 計算複利現值表
def pvif(P):
# pvif( ): 藉由輸入 n 計算並印出 1 到 n 期以及 1 到 n% 的複利現值係數
    print('%6s' %('期數 / 係數'), end = ' ')
    for t in range(1, P + 1):
        print('%6.2f %s' %(t, '%'), end = ' ')
    print( )
    for n in range(1 ,P + 1):
        print('%8d ' %(n), end = ' ')
        for i in range(1 , P + 1):
            pvif_value = 1 / (1 + (i / 100)) ** n
            print('%8.4f ' %(pvif_value), end = ' ')
        print( )
Period = int(input('請輸入期數 = '))
pvif(Period)