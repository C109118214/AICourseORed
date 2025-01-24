# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_excel("0050.xlsx")
df.info()

# 去除不是數值的欄位
df2 = df.drop(["日期"], axis = 1)
# 強迫轉換成數值資料，遇到不能轉換的直接清掉變成空值
df2["漲跌價差"] = pd.to_numeric(df2["漲跌價差"], errors = "coerce")
print(df2.mean())
print(df2.sum())
print(df2.max())
print(df2.min())
print(df2.std())
print(df2.count())
df_des = df2.describe()
print(df_des)
df_des.to_excel("des.xlsx")
# =============================================================================
# print(df2.min()["最高價"])
# print(df2["最高價"].min())
# 
# df3 = df[["開盤價", "收盤價", "最高價", "最低價"]]
# print(df3.sum(axis = 1))
# =============================================================================
