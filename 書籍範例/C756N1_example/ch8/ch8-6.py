# ch8-6: 定義私有方法
class car:
    __fuelvol = 0
    __carmodel = '  '
    def __init__(self, color, style):
        self.color = color
        self.style = style
# 定義私有屬性-油箱容量75與車款RV，名稱前加雙底線
        self.__fuelvol = 75
        self.__carmodel = 'RV休旅車'
# 在方法內呼叫私有屬性
    def fuel(self):
        print(str(self.__carmodel) + '油箱容量 = ' + str(self.__fuelvol))
print('---呼叫類別---')
obj_car = car('黑色', 'BMW')
print(obj_car.color, obj_car.style)
print('---呼叫車款與油箱容量方法---')
obj_car.fuel( )
print('---更改油量容量為35，無效---')
obj_car.__fuelvol = 35
obj_car.fuel( )
# obj_car.__fuelvol  # 呼叫私有屬性會出現AttributeError
# obj_car.__carmodel  