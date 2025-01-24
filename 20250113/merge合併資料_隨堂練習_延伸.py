# -*- coding: utf-8 -*-
import pandas as pd

path = "資料/"
df_sell = pd.read_excel(f"{path}銷售資料.xlsx")
df_cus = pd.read_excel(f"{path}客戶列表.xlsx")

df_sell["年"] = df_sell["日期"].dt.year
df_sell["月"] = df_sell["日期"].dt.month
df_sell["銷售額"] = df_sell["單價"] * df_sell["數量"]
df_sell_group = df_sell.groupby(["年", "月", "客戶編號"])
result_df = df_sell_group["銷售額"].sum()

result_df = result_df.reset_index()

df = pd.merge(left = result_df, # 要查表的資料
              right = df_cus, # 被查表的資料
              left_on = "客戶編號", # 查表對應的欄位
              right_on = "編號"
              )

print(df) # 將貨品名稱溶入進銷售資料中了

# 因為重複，所以只保留客戶編號，刪除編號
df = df.drop(["編號"], axis = 1)


