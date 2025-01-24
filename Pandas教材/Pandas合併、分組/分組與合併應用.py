# -*- coding: utf-8 -*-
import pandas as pd

df_base = pd.read_excel("資料/銷售資料.xlsx")
df_ex = pd.read_excel("資料/擴充銷售資料.xlsx")
print(df_base.shape)
print(df_ex.shape)

df = pd.concat([df_base, df_ex], axis = 0) # 0預設為縱向合併
print(df.shape)

df["銷售額"] = df["單價"] * df["數量"] # 計算銷售額
df["年"] = df["日期"].dt.year # 取得年
df["月"] = df["日期"].dt.month # 取得月

# 以年、月貨品編號將資料分組
df_group = df.groupby(by = ["年", "月", "貨品編號"]) 

df_sales = df_group["銷售額"].mean()
print(df_sales)