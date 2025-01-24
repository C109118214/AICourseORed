# -*- coding: utf-8 -*-
import pandas as pd

path = "資料/"
df_sell = pd.read_excel(f"{path}銷售資料.xlsx")
df_cus = pd.read_excel(f"{path}客戶列表.xlsx")


df = pd.merge(left = df_sell, # 要查表的資料
              right = df_cus, # 被查表的資料
              left_on = "客戶編號", # 查表對應的欄位
              right_on = "編號"
              )

print(df) # 將貨品名稱溶入進銷售資料中了
