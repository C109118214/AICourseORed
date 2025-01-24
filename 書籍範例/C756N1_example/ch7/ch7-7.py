# ch7-7.py功能 : 傳址方式傳遞串列的參數，計算參數平均值
def callbyaddress(number):
# callbyreference 函數功能 : 計算平均新增到傳入參數之後
    print('傳入函數時的內容值記憶體編號 ', number, id(number))
    n = len(number)
    meanv = sum(number) / n
    number.append(meanv)
    print('運算後的記憶體編號 ', number, id(number))
    return number
sample = [5, 8, 9, 6, 4, 1, 5, 3, 6, 2]
print('呼叫函數前的原始值與記憶體編號 ', sample, id(sample))
print('呼叫函數後的內容值 ', callbyaddress(sample))
print('呼叫函數後的原始值也會被改變 ', sample)