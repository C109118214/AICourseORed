# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_csv("iris.csv")
type_list = df["屬種"].unique()
print(type_list)

# 查看每一種有幾筆資料
df_group = df.groupby("屬種")
print(df_group["屬種"].count())


mapper = {}
index = 1
for i in type_list:
    mapper[i] = index
    index+= 1
print(mapper)
df["屬種"] = df["屬種"].replace(mapper)
print(df)
# =============================================================================
# mapper = {"setosa" : 1, "versicolor" : 2, "virginica" :3}
# df["屬種"] = df["屬種"].replace(mapper)
# print(df)
# =============================================================================
