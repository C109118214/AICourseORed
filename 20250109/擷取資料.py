# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_excel("0050.xlsx")

print(df.loc[ [0,4,9,14] , ["日期", "收盤價"] ])
print(df.iloc[ [0,4,9,14] , [0, 6] ])


