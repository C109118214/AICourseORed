# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_excel("0050缺值版.xlsx")

# 算出每個欄位的平均值
df_mean = df.mean()
print(df_mean)

# 算出每個欄位的中位數
df_median = df.median()
print(df_median)

# 將空值填入平均值
df_filled = df.fillna(df_mean )
print(df_filled)

# =============================================================================
# # 將空值填入中位數
# df_filled = df.fillna(df_median )
# print(df_filled)
# =============================================================================
