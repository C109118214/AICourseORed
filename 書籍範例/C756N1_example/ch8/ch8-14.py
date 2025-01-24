# ch8-14: 屬性錯誤
intvalue = 5
# 整數資料型別沒有繼承append( )方法，會引發屬性錯誤
intvalue.append(10)
# print('整數intvalue = ', intvalue)
listvalue = [15]
print('原始串列listvalue = ', listvalue)
# 串列資料型別有繼承append( )方法，不會引發屬性錯誤
listvalue.append(20)
print('新增後串列listvalue = ', listvalue)