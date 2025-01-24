# -*- coding: utf-8 -*-
from scipy.stats import ttest_ind
import pandas as pd
from os import listdir

# 讀取所有驗證集的結果
path = "驗證集結果/"
# 列出資料夾中所有的檔案名稱，回傳一個List
file_list = listdir(path) 

# 將指定的欄位資料整理成dict
# 將欄位的平均也整理成dict
column = "Accuracy" # 要進行T檢定的欄位
col_dict = {}
col_mean_dict = {}
for file in file_list:
    df = pd.read_excel(f"{path}{file}")
    col_dict[file] = df[column]
    col_mean_dict[file] = df[column].mean()

# 裝倆倆T檢定的P-value
Ttest_df = pd.DataFrame()
# 用迴圈讓每種模型的結果倆倆檢定
for k in col_dict.keys():
    for m in col_dict.keys() :
        col_1 = col_dict[k]
        col_2 =  col_dict[m]
        # T 檢定取出P值
        T_test_pvalue = ttest_ind(col_1 , col_2)[1]
        #檢定後用at放入DataFrame中
        Ttest_df.at[k, m] =  T_test_pvalue
        
print(Ttest_df)



