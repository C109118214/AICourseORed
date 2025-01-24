# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["font.size"] = 10
plt.rcParams["font.family"] = ["Arial", "Microsoft Jhenghei"]

df = pd.read_excel("0050.xlsx")

df["日期"] = pd.to_datetime( df["日期"] )
# %Y代表四位數的西元年
# %m代表月份，把月份補0到二位數
# %d代表日，補0到二位數
df["日期"] = df["日期"].dt.strftime("%m-%d")
df.info()

df.plot(kind = "hist",
        y = "漲跌價差",
        bins = 5
        )
plt.title("開盤價與收盤價")
plt.ylabel("價格")
plt.show()
