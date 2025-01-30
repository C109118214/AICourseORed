data = []

with open("read.txt","r") as file:
    # TODO
    max_height = 0
    max_weight = 0
    
    height_list = []
    weight_list = []
    
    for row in file.readlines():
        print(row)
        row = row.replace("\n", "")
        row = row.split(" ")
        
        name, height, weight = row
        height, weight = int(height), int(weight)
        height_list.append(height)
        weight_list.append(weight)
        
        if height > max_height:
            max_height_name = row[0]
            max_height = height

        if weight > max_weight:
            max_weight_name = row[0]
            max_weight = weight

avg_height = sum(height_list) / len(height_list)
avg_weight = sum(weight_list) / len(weight_list)

print(f"Average height: {avg_height:.2f}")
print(f"Average weight: {avg_weight:.2f}")
print(f"The tallest is {max_height_name} with {max_height:.2f}cm")
print(f"The heaviest is {max_weight_name} with {max_weight:.2f}kg")


"""
Average height: _
Average weight: _
The tallest is _ with _cm
The heaviest is _ with _kg
"""