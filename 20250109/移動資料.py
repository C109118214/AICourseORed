# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_excel("0050.xlsx")

df["收盤價T-1"] =  df["收盤價"].shift(1)
df["隔日收盤價"] = df["收盤價"].shift(-1)

df["當日變動百分比"] = df["收盤價"] / df["收盤價T-1"]
df["隔日的漲幅"] = df["隔日收盤價"] / df["收盤價"] - 1
