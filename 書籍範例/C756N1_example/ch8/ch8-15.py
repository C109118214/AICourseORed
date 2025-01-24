# ch8-15: 算術錯誤
import math
print('---除以零錯誤---')
# data = [5, 3, 0]
data = [5, 3, 1]
for i in data: 
    print(10 / i)
print('---浮點數錯誤---')
number = [1.4, 1.3, 1.2]
for i in number: 
    print(i - 1.0)
print('---溢位錯誤---')
expvalue = [1, 10, 100, 1000]
# expvalue = [1, 10, 100]
for i in expvalue:
    print(math.exp(i))