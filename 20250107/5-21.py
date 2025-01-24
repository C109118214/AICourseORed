# -*- coding: utf-8 -*-
learning_rate = 0.4 # 消滅不懂的地方的比率
unknown_rate = 1 # 假設一開始全部不懂
target = 0.1 # 不懂的比率降至10%以下
hours_count = 0
# 當不懂的比率大於目標比率，就繼續讀書
while unknown_rate > target :
    hours_count+= 1 # 累計時數
    unknown_rate *= (1 - learning_rate) # 更新不懂的比率
    print(unknown_rate)

print(f"總共需要{hours_count}小時可以取得90分")