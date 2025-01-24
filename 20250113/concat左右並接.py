# -*- coding: utf-8 -*-
import pandas as pd

path = "資料/"
df_base = pd.read_excel(f"{path}銷售資料.xlsx")
df_ex = pd.read_excel(f"{path}擴充銷售資料.xlsx")
print(df_base.shape)
print(df_ex.shape)

# axis = 1，左右連接，根據index相同進行連接
df = pd.concat( [df_base, df_ex], axis = 1 )
print(df.shape)

