# ch7-8.py功能 : 傳值方式傳遞整數的參數，計算傳進來的參數求平方
def callbyvalue(number):
# callbyvalue 函數功能 : 計算參數乘上自己後回傳 
    print('傳入函數時的內容值記憶體編號 ', number, id(number))
    number *= number
    print('運算後的記憶體編號 ', number, id(number))
    return number
sample = 4
print('呼叫函數前的原始值與記憶體編號 ', sample, id(sample))
print('呼叫函數後的內容值 ', callbyvalue(sample))
print('呼叫函數前的原始值不會被改變 ', sample)