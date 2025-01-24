# -*- coding: utf-8 -*-
import pandas as pd

path = "資料/"
df_sell = pd.read_excel(f"{path}銷售資料.xlsx")
df_good = pd.read_excel(f"{path}商品資料.xlsx")

df = pd.merge(left = df_sell, 
              right = df_good,
              left_on = "貨品編號",
              right_on = "貨品編號"
              )

print(df)