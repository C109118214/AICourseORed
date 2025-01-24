# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_csv("iris.csv")
print(df)

dummy_result = pd.get_dummies(df["屬種"],
                              prefix="屬種",
                              drop_first= True)
dummy_result = dummy_result.astype(int)

df_dummy = pd.concat([df, dummy_result],
                     axis = 1)

df_dummy= df_dummy.drop(["屬種"], axis = 1)

mapper = {"setosa" : 1, "versicolor" : 2, "virginica" :3}
df["屬種"] = df["屬種"].replace(mapper)
print(df)
