# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_excel("0050.xlsx")

for c in df.columns:
    if c in ["日期"]:
        print("跳過日期了")
        continue
    print(c)
    #print(df[c])

for i in df.index:
    print(i)
    print(df.loc[i])

# 走訪每一列，分成索引(index)與對應的資料(row)
for index, row in df.iterrows():
    print(index)
    print(row)
    print("========")
    
# 走訪每一列，分成索引(index)與對應的資料(row)
for index, row in df.iterrows():
    print(index)
    for c in df.columns:
        print(row[c])
    print("========")