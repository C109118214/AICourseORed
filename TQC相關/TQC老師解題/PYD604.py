# TODO
number_list = []
for i in range(10):
    num = input()
    number_list.append(num)

max_count = 0
for num in number_list:
    count = number_list.count(num)
    if count > max_count:
        mode = num
        max_count = count

# 輸出結果
print(mode)
print(max_count)
