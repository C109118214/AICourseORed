# ch8-16: 索引錯誤與鍵錯誤
print('---索引錯誤---')
data = [5, 3, 1]
for i in range(len(data)):
    # print(data[i+1])
    print(data[i])
print('---鍵錯誤---')
dicdata = {2330:'台積電', 1101: '台灣水泥', 3008: '大立光'}
ids = [2330, 1101, 3008, 2317]
# ids = [2330, 1101, 3008]
for i in ids:
    print(dicdata[i])