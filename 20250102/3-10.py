# -*- coding: utf-8 -*-
age = 18
result = "%s%d%s" % ("聖嘉今年", age, "歲")
print(result)
#占位符號

result = f"聖嘉今年{age}歲"
print(result)

price = 123.4567
print("價格為%.2f元" % price)

price = 123.4567
print("價格為%08.2f元" % price)

id_num = 1
# 補0到第四位
print("您的編號為%04d" % id_num)

id_num = 1
# 補空格到第四位
print("您的編號為%4d" % id_num)