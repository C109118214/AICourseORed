# ch8-2: 呼叫類別產生物件實體
import numpy as np
class car:
# 初始化方法，當產生實體的時候這個方法自動被呼叫
# 用self.xxx來定義實體的屬性，每個被建立的實體會有自己的屬性
    def __init__(self, color, style):
        self.color = color
        self.style = style
print('---呼叫類別產生一個物件實體---')
obj_single = car('灰色', 'Altis')
print(obj_single.color, obj_single.style)
print('---連續呼叫類別產生多個物件實體---')
data = np.array([['黑色', '賓士'],['白色', 'Lexus'],['紅色', '法拉利']])
for i in range(len(data)):
    obj_multi = car(data[i,0], data[i,1])
    print(obj_multi.color, obj_multi.style )