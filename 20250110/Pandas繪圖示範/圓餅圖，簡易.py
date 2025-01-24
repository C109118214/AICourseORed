# -*- coding: utf-8 -*-
import pandas as pd

data_dict = {
    "項目" : ["0-19", "20-39", "40-64", "65以上"],
    "人數" : [20, 40, 50, 30]
    }

df = pd.DataFrame(data_dict )
# 因為會自動把index當成圖例，所以把index指定成項目欄位
df.index = df["項目"]
df["人數"].plot(kind = "pie",
              autopct='%1.2f%%') # 顯示百分比
