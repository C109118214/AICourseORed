# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_excel("0050.xlsx")

print(df.head())
print(df.tail(3))

# ascending預設為True，升冪排序(由小到大)
# ascending為False，降冪排序(由大到小)
sorted_df = df.sort_values(by = ["收盤價", "日期"], ascending = [False, True])