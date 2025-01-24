# -*- coding: utf-8 -*-
import random as rd

# 產生一個1到42的串列，模擬彩球池
Number_pool = list(range(1,43))
result_list = [] # 開獎結果
for i in range(6):
    Number_len = len(Number_pool) # 當下還有幾個彩球
    print(Number_pool)
    print(Number_len)
    # 抽出彩球對應的序列號(index)
    Number_index = rd.randint(0, Number_len - 1)
    # 根據抽出來的序列號，選出號碼，取後不放回
    Num = Number_pool.pop(Number_index)
    #將號碼放入開獎結果
    result_list.append(Num)

print(result_list)
result_list.sort()
print(result_list)