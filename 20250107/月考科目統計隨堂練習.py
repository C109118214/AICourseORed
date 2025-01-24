# -*- coding: utf-8 -*-

list_1 = ["國", "數", "英", "數", "國",
          "數", "英", "數", "英", "國"]

dict_1 = {}

for i in list_1:# 走訪科目列表
    # 如果這個科目，沒有在字典中
    # 新增這個科目，key為科目名稱，value為1，代表累積第一次
    if i not in dict_1.keys():
        dict_1[i] = 1
    else:
        dict_1[i]+= 1
    print(i, dict_1, dict_1.keys())

print(dict_1)

