# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_excel("資料/銷售資料.xlsx")

df_group = df.groupby(by = ["貨品編號"]) # 將資料以貨品編號分組
print(df_group[["單價", "數量"]].mean())
print("------------")

def cost(data):
    # 傳入的data格式為Series或DataFrame
    return data.mean() * 0.5 # 假設成本價是50%，計算成本

apply_result = df_group["單價"].apply(cost) # 帶入單價來計算成本
print(apply_result)
print("------------")

agg_dict = {"單價" : ['mean'],
            "數量" : ['sum','mean']
            }
agg_result = df_group.agg(agg_dict)
print(agg_result)
print("------------")