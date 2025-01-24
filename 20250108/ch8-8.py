# ch8-8: 改寫父類別的方法
class vehicle( ):
    def __init__(self, color, style):
        self.color = color
        self.style = style
    def start(self):
        print('啟動車子')
        return ('啟動完成')
    def driving(self):
        print('前進車子')
        return ('前進中')
    def brake(self):
        print('停止車子')
        return ('刹車完成')
# 改寫子類別
class rv(vehicle):
    # 改寫初始代方法
    def __init__(self, color, style):
        self.color = color
        self.style = style
        self.skylight = '含天窗'
class firetruck(vehicle):
    # 新增天梯方法
    def ladder(self):
        self.floors= 20
        return('雲梯有' + str(self.floors) + '層樓高')
print('---呼叫類別物件實體與方法---')
obj_rv = rv('黑色', '休旅車')
print('這款是' + obj_rv.color + obj_rv.style + obj_rv.skylight)
print(obj_rv.brake( ))
print('---呼叫類別物件實體與方法---')
obj_firetruck = firetruck('紅色', '消防車')
print('這款是' + obj_firetruck.color + obj_firetruck.style, end = '')
print(obj_firetruck.ladder( ))
print(obj_firetruck.start( ))