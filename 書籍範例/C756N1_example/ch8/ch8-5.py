# ch8-5: 封裝類別，定義私有方法
class car:
    def __init__(self, color, style):
        self.color = color
        self.style = style
# 定義一個私有方法updateGPS( )，名稱前加雙底線
    def __updateGPS(self):
        print('GPS地圖程式更新')
    def stopping(self):
        print('停車')
        self.__updateGPS( )
print('---呼叫類別---')
obj_car = car('黑色', 'BMW')
print(obj_car.color, obj_car.style)
obj_car.stopping( )
# obj_car.__updateGPS( )  # 無法藉由物件實體存取私有方法