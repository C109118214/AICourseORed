# TODO

print("Create tuple1:")
# TODO
list_1 = []
while True: # 預設為無窮迴圈
    num = int(input())
    if num == -9999:# 直到num是-9999為止
        break # 結束迴圈
    
    list_1.append(num) # 每次輸入的整數都放進list_1中
    
print("Create tuple2:")
list_2 = []
while True: # 預設為無窮迴圈
    num = int(input())
    if num == -9999:# 直到num是-9999為止
        break # 結束迴圈
    
    list_2.append(num) # 每次輸入的整數都放進list_1中

# 將兩個串列合併
list_merge = list_1 + list_2
 # 將合併的串列轉成tuple
tuple_1 = tuple(list_merge)
list_merge.sort() # 將串列排序
# 輸出結果
print(f"Combined tuple before sorting: {tuple_1}")
print(f"Combined list after sorting: {list_merge}")
# TODO


"""
Combined tuple before sorting: _
Combined list after sorting: _
"""
