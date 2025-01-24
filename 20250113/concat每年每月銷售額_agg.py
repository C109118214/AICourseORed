# -*- coding: utf-8 -*-
import pandas as pd

path = "資料/"
df_base = pd.read_excel(f"{path}銷售資料.xlsx")
df_ex = pd.read_excel(f"{path}擴充銷售資料.xlsx")

# 上下連接，根據column相同進行連接
df = pd.concat( [df_base, df_ex])
df.info() # 確認日期格式是不是datetime，不是的話用pd.to_datetime轉換
df["銷售額"] = df["單價"] * df["數量"]
df["年"] = df["日期"].dt.year
df["月"] = df["日期"].dt.month

df_group = df.groupby(["年", "月", "貨品編號"])

agg_dict = {"銷售額" : ["sum", "mean"],
            "數量"  : ["sum", "mean"]
            }

result = df_group.agg(agg_dict)

result.to_excel("每年每月貨品銷售額_agg.xlsx")