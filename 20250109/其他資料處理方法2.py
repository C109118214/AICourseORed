# -*- coding: utf-8 -*-
import pandas as pd

data_dict = {
    "項目" : ["蘋果", "橘子", "西瓜", "西瓜"],
    "數量" : [2,3,1,1],
    "儲存倉庫" : ["A", None, "B", "C"]
    }

df = pd.DataFrame(data_dict)

# "項目"與"數量"中有重複的就刪除，預設是保留第一筆數值
print(df.drop_duplicates(subset=["項目", "數量"]))
# 要保留重複的最後一筆數值，加上keep = "last"
print(df.drop_duplicates(subset=["項目"], keep = "last"))

# 只要那一列(row)資料，有空值的，那就刪除那筆資料
print(df.dropna())

# 只要那一列(row)的項目欄位是空值，那就刪除該資料
print(df.dropna(subset=["項目"]))
# 數量或儲存倉庫那一列任何一個是空值，就刪除資料
print(df.dropna(subset=["數量", "儲存倉庫"]))

# 將空值填上指定的值
print( df.fillna("C") ) # 只要有空值就填入C
print( df["儲存倉庫"].fillna("D") ) # 只要有空值就填入D
print( df.ffill() )# 填入上一筆不是空值的值
print( df.bfill() )# 填入下一筆不是空值的值