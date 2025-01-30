# TODO

print("Create tuple1:")
tuple1 = []
while (num := int(input())) != -9999:
    tuple1.append(num)

tuple1 = tuple(tuple1)

print("Create tuple2:")
tuple2 = []
while (num := int(input())) != -9999:
    tuple2.append(num)

tuple2 = tuple(tuple2)

combined_tuple = tuple1 + tuple2
sorted_list = sorted(combined_tuple)

print(f"Combined tuple before sorting: {combined_tuple}")
print(f"Combined list after sorting: {sorted_list}")



"""
Combined tuple before sorting: _
Combined list after sorting: _
"""
