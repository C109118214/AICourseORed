# ch8-4: 靜態方法的呼叫方式
class car:
# 靜態方法不需要先建立物件實體，直接呼叫類別.方法
    @staticmethod
    def driving( ):
        print('前進車子')
print('---呼叫 靜態.方法( )---')
car.driving( )