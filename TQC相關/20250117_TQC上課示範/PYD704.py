# TODO
set_1 = set() # 空的set一定要用set()，不能用{}，
# 因為會被認為是空字典
while True:
    num = int(input())
    if num == -9999:
        break
    set_1.add(num) # 將輸入的整數放入set
Length = len(set_1)
Max = max(set_1)
Min = min(set_1)
Sum = sum(set_1)

print(f"Length: {Length}")
print(f"Max: {Max}")
print(f"Min: {Min}")
print(f"Sum: {Sum}")   




"""
Length: _
Max: _
Min: _
Sum: _
"""
