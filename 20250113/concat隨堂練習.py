# -*- coding: utf-8 -*-
import pandas as pd

path = "資料/"
df_base = pd.read_excel(f"{path}銷售資料.xlsx")
df_ex = pd.read_excel(f"{path}擴充銷售資料.xlsx")

# 上下連接，根據column相同進行連接
df = pd.concat( [df_base, df_ex])

df["銷售額"] = df["單價"] * df["數量"]

df_group = df.groupby("客戶編號")

print(df_group["銷售額"].sum())