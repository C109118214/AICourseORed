# ch8-3: 類別方法的呼叫方式
class car:
# 類別方法不需要先建立物件實體，直接呼叫類別.方法
    @classmethod
    def start(cls):
        print('啟動車子')
print('---呼叫 類別方法( )---')
car.start( )