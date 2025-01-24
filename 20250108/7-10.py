# -*- coding: utf-8 -*-
def callbyvalue(number):
    print("傳入的number的記憶體編號",number, id(number))
    number *= number
    print("函數運算完成後的記憶體編號",number, id(number))
    return number

sample = 4
print("呼叫函數前的內容值與記憶體編號",sample, id(sample))
callbyvalue(sample)
print("呼叫函數後的內容值與記憶體編號",sample, id(sample))
