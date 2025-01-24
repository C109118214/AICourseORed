# -*- coding: utf-8 -*-
import pandas as pd

path = "資料/"
df_base = pd.read_excel(f"{path}銷售資料.xlsx")
df_ex = pd.read_excel(f"{path}擴充銷售資料.xlsx")
print(df_base.shape)
print(df_ex.shape)

df = pd.concat( [df_base, df_ex] )
print(df.shape)

# 重新把index變成從0開始編號，drop = True不保留原本的index
df = df.reset_index(drop = True)