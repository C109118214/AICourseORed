# -*- coding: utf-8 -*-
import pandas as pd

df = pd.DataFrame() # 空的df

# 在index為1和2的日期欄位放入資料
df.loc[1, "日期"] = "2025/01/09"
df.at[2, "日期"] = "2025/01/09"
# 插入欄位，長度要與原本的DF資料數一致
df["價格"] = [100,105]

