# ch8-13: 型別錯誤
buydate = '20201209'
selldate = 20201215
# selldate = '20201215'
print('buydate = ', type(buydate))
print('selldate = ', type(selldate))
# 字串與整數做關係運算是不被允許的
if buydate < selldate:
    print('先買後賣')
openprice = 50.03
closeprice = 50
print(type(openprice))
print(type(closeprice))
# 浮點數與整數是被允許的
if openprice > closeprice:
    print('買進')
# 字串與整數相加是不被允許的
print(buydate + openprice)
# print(openprice + closeprice )