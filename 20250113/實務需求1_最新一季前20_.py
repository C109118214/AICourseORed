# -*- coding: utf-8 -*-
import pandas as pd


Excel_file = pd.ExcelFile("需求1_行業別客戶別排序.xlsx")
sheet_list = Excel_file.sheet_names

for i in sheet_list:
    # index_col = 0指定第一個欄位為index
    df = pd.read_excel(Excel_file, sheet_name = i, index_col = 0)
    newest_data = df.iloc[:, -1].dropna() # 去除空值
    # 計算前20%
    data_len = len(newest_data)
    data_len_20 = int( data_len * 0.2 )
    # 由小到大的排序
    newest_data = newest_data.sort_values(ascending = False)
    print(i, newest_data[:data_len_20])
