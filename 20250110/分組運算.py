# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_excel("資料/銷售資料.xlsx")
df["銷售額"] = df["單價"] * df["數量"]
print(df)
# 根據貨品編號進行分組
df_group = df.groupby("貨品編號")

print(df_group[ ["單價", "數量"] ].mean())
print(df_group[ [ "銷售額", "數量"] ].sum())