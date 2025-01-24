# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_excel("0050.xlsx")

df["價差"] = df["最高價"] - df["最低價"]
print(df["價差"].mean())
print(df["價差"].std())