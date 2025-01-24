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
        self.__car_id = "1234" # 私有屬性
    
    def forward(self, speed):
        print(self.color,self.style,"以時速",speed,"公里/小時前進")
        
    def back(self):
        print(self.color,self.style,"倒車")
    
    # 私有方法
    def __update_GPS(self):
        print("更新GPS")
    
    def call_update_GPS(self):
        # 私有屬性與方法只能在物件內呼叫
        print(self.__car_id)
        self.__update_GPS()
        
Car_1 = Car("紅色", "法拉利")
print(Car_1.color)
print(Car_1.style)
Car_1.forward(80)
Car_1.call_update_GPS()
#Car_1.__update_GPS() # 無法直接在物件外呼叫私有方法
# 可以用_類別名稱__私有屬性或方法的方式呼叫
print(Car_1._Car__car_id)
Car_1._Car__update_GPS()

print("----------")
Car_2 = Car("白色", "保時捷")
print(Car_2.color)
print(Car_2.style)
Car_2.back()

