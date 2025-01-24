# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_csv("pima.csv")
df.info()

print(pd.get_dummies(df["是否有糖尿病"],
                     prefix = "是否有糖尿病",
                     drop_first=True) )

mapper = {"是": 1, "否":0}
print(df["是否有糖尿病"].replace(mapper))

