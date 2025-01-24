
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

df_group = df.groupby( ["年", "月", "貨品編號"] )

result = df_group["銷售額"].mean()
# 將分組的index，放入欄位，重新設定index為從0開始編號
result = result.reset_index()
result.to_excel("每年每月貨品銷售額.xlsx", index = False)