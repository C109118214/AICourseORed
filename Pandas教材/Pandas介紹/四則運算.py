# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_excel("0050.xlsx")

df["加"] = df["開盤價"] + df["收盤價"]
df["減"] = df["最高價"] - df["最低價"]
df["乘"] = df["成交股數"] * df["收盤價"]
df["除"] = df["最高價"] / df["最低價"]

print(df[ ["加", "減", "乘", "除"] ])

df["成交張數"] = df["成交股數"] // 1000