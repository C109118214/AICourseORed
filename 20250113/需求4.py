# -*- coding: utf-8 -*-
import pandas as pd

# 讀取資料
all_sheets_df = pd.read_excel("需求3_分產業別、客戶每個月總銷售額整理.xlsx",
                              sheet_name=None,
                              index_col = 0)

# 需求4 客戶業績變化

# 走訪每張工作表
with pd.ExcelWriter("需求4_客戶業績變化.xlsx",mode = "w") as writer:
    for sheet_name, df in all_sheets_df.items():
        result_df = pd.DataFrame()
        for c in df.columns:
            cus_order = df[c][df[c] > 0]

            max_sales = 0
            MDD = 0
            for i in cus_order:
                if i > max_sales:
                    max_sales = i
                
                diff = max_sales - i
                if  diff > MDD:
                    MDD = diff
                
            result_df.at[c, "Max"] = max_sales
            result_df.at[c, "MDD"] = MDD
            
        result_df = result_df.sort_values(by = "MDD", ascending = False)
        result_df.to_excel(writer, sheet_name = sheet_name)