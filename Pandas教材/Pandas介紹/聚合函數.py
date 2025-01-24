# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_excel("0050.xlsx")
df.info()
# 去除不是數值的欄位
df2 = df.drop(["日期", "漲跌價差"], axis = 1)
print(df2.mean())
print(df2.sum())
print(df2.max())
print(df2.min())

print(df2.min()["最高價"])
print(df2["最高價"].min())

df3 = df[["開盤價", "收盤價", "最高價", "最低價"]]
print(df3.sum(axis = 1))