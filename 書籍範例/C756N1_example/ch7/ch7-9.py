# ch7-9.py 功能 : 實際參數與形式參數的函數傳遞參數範例
def polyequ(x):
# polyequ: 計算 (x ** 2) + (4 * x) + 6 以運算式的結果回傳
    return(x ** 2) + (4 * x) + 6
sample = 4
result = polyequ(sample)
print('呼叫函數( x ** 2 ) + ( 4 * x ) + 6 = ', result)