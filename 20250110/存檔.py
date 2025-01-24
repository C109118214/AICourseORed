# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_excel("0050.xlsx")
print(df)

df.to_csv("0050.csv",index = False)