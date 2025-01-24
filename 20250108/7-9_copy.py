# -*- coding: utf-8 -*-
def callbyaddress(number):
    number = number.copy()# 如果不想動到原始資料，可以用copy複製一份
    print("傳入的number的記憶體編號", id(number))
    n = len(number)
    meanv = sum(number) / n
    number.append(meanv)
    print("函數運算完成後的記憶體編號", id(number))
    return number

sample = [5,8,9,6,4,1,5,3,6,2]
print("呼叫函數前的內容值與記憶體編號",sample, id(sample))
callbyaddress(sample)
print("呼叫函數後的內容值與記憶體編號",sample, id(sample))
