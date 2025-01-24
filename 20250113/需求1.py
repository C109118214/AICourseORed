# -*- coding: utf-8 -*-
import pandas as pd

# 讀取資料
Data_path = "零售資料/"
Item_df = pd.read_csv(f"{Data_path}貨品資料.csv")
Salesperson_df = pd.read_csv(f"{Data_path}貨品資料.csv")
Customer_df = pd.read_csv(f"{Data_path}客戶資料.csv")
Fact_df = pd.read_csv(f"{Data_path}銷貨資料_fact_table.csv")

# 需求1 找出客戶依行業分組之銷售額當季前20%大客戶
# 將銷售資料與客戶的資料合併，以便根據產業分組
Industry_df = pd.merge(left = Fact_df,
                       right = Customer_df,
                       left_on = "Customer_ID",
                       right_on = "Customer_ID"
                       )

# 銷售額
Industry_df["Sales_Amount"] = Industry_df["Quantity"] * Industry_df["Unit_price"]
Industry_group = Industry_df.groupby(by = ["Industry", "Customer_ID"])

Industry_Sales_sum = Industry_group["Sales_Amount"].sum()

# 走訪第一層index，"Industry"
with pd.ExcelWriter("需求1_行業別客戶別排序.xlsx",mode = "w") as writer:
    for i in Industry_Sales_sum.index.levels[0]:
        ind_group_df = Industry_Sales_sum[i] # 取出個別產業的資料
        ind_group_df = ind_group_df.sort_values(ascending = False) # 遞減排序
        ind_group_df_top_num = int(ind_group_df.count() * 0.2) # 計算當組前20%的數量
        ind_group_df = ind_group_df[:ind_group_df_top_num] # 篩選前20%資料
        ind_group_df.to_excel(writer, sheet_name = i) # 存檔


