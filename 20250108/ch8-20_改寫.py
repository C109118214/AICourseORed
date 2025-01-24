# ch8-20: 以自訂函數撰寫排列組合，加入異常處理機制
def fact (k) :
 # fact: 計算階層
    if k <= 0:
        raise ValueError('輸入的參數 m 必須大於 n 哦')
    else:
        prodi = 1
        for i in range (k, 1, -1):
            prodi *= i
    return(prodi) 
while True: 
    try: 
        m = int(input('輸入正整數 m = ')) 
        n = int(input('輸入正整數 n = ')) 
        number = fact(m) / (fact(n) * fact(m - n)) 
        print('%s%d%s'%('排列組合共有', number, '方法')) 
        break
    
    except ValueError as v:
        print('數值錯誤，' + str(v))
    
    print('------------------------------')
