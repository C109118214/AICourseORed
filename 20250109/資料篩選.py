# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_excel("0050.xlsx")

print( df["收盤價"] > 135 )

print(df[ df["收盤價"] > 135 ] )

filter_condition = df["收盤價"] > 135
filter_condition_2 = df["最高價"] > 138

print(df[ filter_condition ])
# &代表and，條件記得用()包覆起來
print(df[ (df["收盤價"] > 135) &
         (df["最高價"] > 138) ] )

print(df[ filter_condition &
         filter_condition_2 ] )

# |代表or，條件記得用()包覆起來
print(df[ filter_condition |
         filter_condition_2 ] )