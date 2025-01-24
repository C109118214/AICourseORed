# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_excel("0050.xlsx")
print(df)

df.info()
print("========")
print(df.shape)
print(df.shape[0])
print(df.shape[1])
print("========")
print(df.index)
print("========")
print(df.columns)