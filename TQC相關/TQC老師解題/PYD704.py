# TODO

num_list = []
while True:
    num = int(input())
    if num == -9999:
        break
    num_list.append(num)
num_set = set(num_list)
print(f"Length: {len(num_set)}")
print(f"Max: {max(num_set)}")
print(f"Min: {min(num_set)}")
print(f"Sum: {sum(num_set)}")


"""
Length: _
Max: _
Min: _
Sum: _
"""
