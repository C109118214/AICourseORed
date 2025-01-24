# -*- coding: utf-8 -*-
import random as rd
# 蒐集到的不重複公仔
collected_set = set()

count = 0
# 每有蒐集齊全，則繼續抽，當蒐集齊全(6<6 = False)，則結束
while len(collected_set) < 6:
    count+= 1 # 記錄抽獎次數
    num = rd.randint(1, 6) # 抽獎
    collected_set.add(num) # 將抽到的號碼放入集合中，會自動去重複
    print(f"第{count}次抽到{num}號，蒐集了{collected_set}")
    
print(f"總共抽了{count}次")

