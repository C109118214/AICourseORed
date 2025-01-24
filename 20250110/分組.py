# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_excel("資料/銷售資料.xlsx")
print(df)
# 根據貨品編號進行分組
df_group = df.groupby("貨品編號")
print(df_group)
# 分組的組別列表
group_keys = df_group.groups.keys()

for k in group_keys:
    print(k,df_group.get_group(k))
