# -*- coding: utf-8 -*-
# 不一定需要()
class Car:
    # 建構子，初始化物件的屬性
    # 從外面傳入的變數處理
    # self代表這個物件本身
    def __init__(self, color, style):
        # 將傳入的值與物件的屬性連結
        self.color = color
        self.style = style
    
    def forward(self, speed):
        print(self.color,self.style,"以時速",speed,"公里/小時前進")
        
    def back(self):
        print(self.color,self.style,"倒車")
        
        
Car_1 = Car("紅色", "法拉利")
print(Car_1.color)
print(Car_1.style)
Car_1.forward(80)

Car_2 = Car("白色", "保時捷")
print(Car_2.color)
print(Car_2.style)
Car_2.back()

