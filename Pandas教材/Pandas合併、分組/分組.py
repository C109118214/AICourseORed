# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_excel("資料/銷售資料.xlsx")

df_group = df.groupby(by = ["貨品編號"]) # 以貨品編號將資料分組

group_keys = df_group.groups.keys() # 分組後每一組的key
print(group_keys)
print("-------------")

for k in group_keys:
    df_goods = df_group.get_group(k)
    print(df_goods) # 取出每一組的df
    print("-------------")