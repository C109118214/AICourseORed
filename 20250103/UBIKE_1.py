# -*- coding: utf-8 -*-

hours = int(input("請輸入借用了幾小時："))
mins = int(input("請輸入借用了幾分鐘："))

mins = hours * 60 + mins

# 看有幾個30分鐘，不滿30分鐘以30分鐘計費
if mins % 30 != 0:
    cost_sets = mins // 30 + 1
else:
    cost_sets = mins // 30
    
range_1 = 8 * 10
range_2 = 8 * 20

if cost_sets <= 8:
    result = 10 * cost_sets
elif cost_sets <= 16:
    result = range_1 + (cost_sets - 8) * 20
else:
    result = range_1 + range_2 + (cost_sets - 16) * 40
    
print(f"總共{result}元")


