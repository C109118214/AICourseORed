# -*- coding: utf-8 -*-
import pandas as pd

file_path = "資料/"

df_sell = pd.read_excel(f"{file_path}銷售資料.xlsx")
df_goods = pd.read_excel(f"{file_path}商品資料.xlsx")
print(df_sell)
print(df_goods)

# 合併資料
df_merge = pd.merge(left = df_sell,
                    right = df_goods,
                    left_on = "貨品編號",
                    right_on = "貨品編號"
                    )
df_merge = df_merge.sort_values(by = ["日期"])
print(df_merge)

