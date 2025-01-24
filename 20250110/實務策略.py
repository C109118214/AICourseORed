# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_excel("0050.xlsx")

# 買賣價格
df["隔日開盤價"] = df["開盤價"].shift(-1)
df["賣出收盤價"] = df["收盤價"].shift(-5)
# 刪除沒有買賣價格的資料
df = df.dropna(subset = ["隔日開盤價", "賣出收盤價"])

# 篩選符合進場條件的資料
df = df[(df["收盤價"] > 135) &
        (df["最低價"] > 133)
        ]

# 計算買賣獲利
df["損益"] = (df["賣出收盤價"] - df["隔日開盤價"]) * 1000
print("總損益", df["損益"].sum())
print("平均損益", df["損益"].mean())
print("交易次數",df["損益"].count())
