# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_excel("0050.xlsx")
print(df.loc[[1,2,3], ["日期", "開盤價"]])
print(df.iloc[[1,2,3], [0, 3]])

print(df.iloc[1:4, [0,3]])
print(df.loc[1:3, ["日期", "開盤價"]])

print(df.loc[1:4, "日期":"開盤價"])

print(df[["日期", "收盤價"]])
print(df.loc[:, ["日期", "收盤價"]])

print(df.iloc[2:10:2])
print(df.iloc[2::2])
print(df.iloc[::2])
# =============================================================================
# df.index = df["日期"]
# print(df)
# print(df.loc["2021-01-05":"2021-01-07", "日期":"開盤價"])
# print(df.iloc[1:4, [0,3]])
# =============================================================================
