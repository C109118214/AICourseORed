# -*- coding: utf-8 -*-
import pandas as pd

data_dict = {
    "項目" : ["蘋果", "橘子", "西瓜"],
    "數量" : [2,3,1]
    }

df = pd.DataFrame(data_dict)
print(df)