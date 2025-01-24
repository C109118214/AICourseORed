data = []

with open("read.txt","r") as file:
    # TODO
    # 把每一列的資料放入list中
    # readlines，有S
    lines = file.readlines()
    for row in lines:
        print(row)
        # 去除換行符號
        row = row.replace("\n", "")
        row = row.split(" ")
        data.append(row)
       
    height_list = []
    weight_list = []
    max_height = 0
    max_weight = 0
    
    for row in data:
        height = int(row[1])
        height_list.append(height)
        
        weight = int(row[2])
        weight_list.append(weight)
        
        if height > max_height:
            max_height = height
            max_height_name = row[0]
        
        if weight > max_weight:
            max_weight = weight
            max_weight_name = row[0]
    
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