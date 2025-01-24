x = eval(input())
y = eval(input())
z = eval(input())

# TODO
# 統一換成秒數，相加後，再換成小時
hours = (x * 60 + y) / 3600
Speed = z / hours # 計算時速為Speed公里/小時
Speed = Speed / 1.6 # 將Speed公里/小時換成英里/小時
print(f"Speed = {Speed:.1f}")

"""
Speed = _
"""