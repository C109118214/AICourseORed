# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_excel("資料/銷售資料.xlsx")
df["銷售額"] = df["單價"] * df["數量"]
print(df)
# 根據貨品編號進行分組
df_group = df.groupby("客戶編號")

df_total = df_group[ [ "銷售額", "數量"] ].sum()
df_total = df_total.sort_values(by = ["銷售額"],ascending = [False])
df_mean = df_group[ [ "銷售額", "數量"] ].mean()
df_mean = df_mean.sort_values(by = ["銷售額"],ascending = [False])

agg_dict = {
    "銷售額" : ["sum", "mean"],
    "數量" : ["sum", "mean"]
    }
agg_result = df_group.agg(agg_dict)
print(agg_result)
