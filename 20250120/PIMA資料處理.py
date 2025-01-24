# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_csv("pima.csv")
df.info()

# =============================================================================
# print(pd.get_dummies(df["是否有糖尿病"],
#                      prefix = "是否有糖尿病",
#                      drop_first=True) )
# 
# =============================================================================
mapper = {"是": 1, "否":0}
df["是否有糖尿病"] = df["是否有糖尿病"].replace(mapper)

for c in df.columns:
    if c == "懷孕":
        df[c] = df[c].fillna(0)
    else:
        df[c] = df[c].fillna(df[c].mean())

df.to_excel("fillna_pima.xlsx", index = False)