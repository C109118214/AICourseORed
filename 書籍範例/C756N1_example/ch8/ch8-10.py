# ch8-10: 多型
class vehicle( ):
    def __init__(self, color, style):
        self.color = color
        self.style = style
    def __str__(self):
        return('車款名稱: '+self.color + self.style + ', 剎車系統: ')
class car(vehicle):
    def brake(self):
        self.brakesystem = '防鎖死煞車'
        return (super( ).__str__( ) + self.brakesystem)
class firetruck(vehicle):
    def brake(self):
        self.brakesystem = '伺服煞車'
        return (super( ).__str__( ) + self.brakesystem)
class bus(vehicle):
    def brake(self):
        self.brakesystem = '氣壓煞車'
        return (super( ).__str__( ) + self.brakesystem)
class rv(vehicle):
    def brake(self):
        self.brakesystem = '油壓煞車'
        return (super( ).__str__( ) + self.brakesystem)
print('---呼叫多型類別---')
brake_list = [car('黃色', '轎車'), firetruck('紅色', '消防車'),bus('綠色', '公車'), 
                 rv('藍色', '休旅車')]
for i in brake_list:
    print(i.brake( ))