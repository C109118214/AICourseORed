# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_excel("資料/銷售資料.xlsx")
print(df)

df_group = df.groupby("貨品編號")

def cost(data):
    print(data) # 代表每個group的單價、數量欄位(DataFrame)
    print("--------")
    return data.mean() * 0.5

apply_result = df_group[["單價", "數量"]].apply(cost)
print(apply_result)

print(df_group[["單價", "數量"]].mean())