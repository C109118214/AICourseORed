# ch7-23.py 功能: 以自訂函數撰寫排列組合
def fact(k):
# fact: 計算階層
    prodi = 1
    for i in range(k, 1 , - 1):
        prodi *= i
    return(prodi)
m = int(input('輸入 m = '))
n = int(input('輸入 n = '))
number = fact(m) / (fact(n) * fact(m - n))
print('%s %d %s' % ('排列組合共有', number ,'方法'))