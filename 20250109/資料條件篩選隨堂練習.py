# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_excel("0050.xlsx")

# 算出兩個比較值，算出來後都是浮點數(float)
open_mean = df["開盤價"].mean()
close_mean = df["收盤價"].mean() 

condition_1 = df["開盤價"] > open_mean
condition_2 = df["收盤價"] > close_mean

print(df[condition_1 & condition_2])