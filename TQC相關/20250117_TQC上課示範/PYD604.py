# TODO
num_list = []
for i in range(10):
    num = int(input())
    num_list.append(num)
    
max_count = 0 # 紀錄出現最多的次數

for num in num_list:

    num_count = num_list.count(num) # 數字在list中出現的次數
    # 這個數字線的次數比之前的出現最多的次數還多
    # 更新資訊
    if num_count > max_count:
        result = num # 更新眾數 
        max_count = num_count # 更新最多出現的次數

print(result)
print(max_count)