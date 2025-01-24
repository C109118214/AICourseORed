# -*- coding: utf-8 -*-
import pandas as pd
# 需求1 找出客戶依行業分組之銷售額當季前20%大客戶
# 將銷售資料與客戶的資料合併，以便根據產業分組

Data_path = "零售資料/"
Item_df = pd.read_csv(f"{Data_path}貨品資料.csv")
Customer_df = pd.read_csv(f"{Data_path}客戶資料.csv")
Fact_df = pd.read_csv(f"{Data_path}銷貨資料_fact_table.csv")

Fact_df.info() # 查看每個欄位的型別

Fact_df["Date"] = pd.to_datetime(Fact_df["Date"])
Fact_df["year"] = Fact_df["Date"].dt.year
Fact_df["Season"] = Fact_df["Date"].dt.quarter # 找出第幾季
# 將2019、1轉變成201901，減少分組的複雜度
Fact_df["Year_Season"] = Fact_df["year"] * 100 + Fact_df["Season"]
Fact_df = Fact_df.drop(["year", "Season"], axis = 1)


# 銷售額
Fact_df["Sales_Amount"] = Fact_df["Quantity"] * Fact_df["Unit_price"]

Cus_df = Customer_df.drop(["Customer_name"], axis = 1)
df = pd.merge(left = Fact_df,
              right = Cus_df,
              left_on = "Customer_ID",
              right_on = "Customer_ID"
              )

# 計算每個產業，每年每季，每個客戶的總銷售額
Fact_group = df.groupby(["Industry", "Year_Season", "Customer_ID"])
result = Fact_group["Sales_Amount"].sum()

with pd.ExcelWriter("需求1_行業別客戶別排序.xlsx",mode = "w") as writer:
    for ind in result.index.get_level_values(0).unique():
        ind_Ys_df = pd.DataFrame() # 空的DF
        ind_df = result[ind] # 從result，取出那個產業的資料
        for Ys in ind_df.index.get_level_values(0).unique():
            ind_Ys_df[Ys] = ind_df[Ys]
            print(ind_Ys_df)
            print("-------")

        ind_Ys_df.to_excel(writer, sheet_name = ind)
# =============================================================================
# result = result.reset_index()
# 
# result_group = result.groupby(["Industry", "Year_Season"])
# =============================================================================

# =============================================================================
# ind_year_month_list = result.index
# # 提取前三個層級的值
# level1 = result.index.get_level_values(0)
# level2 = result.index.get_level_values(1)
# level3 = result.index.get_level_values(2)
# 
# # 組合前三層的值為唯一列表
# unique_values = list(set(zip(level1, level2, level3)))
# print(unique_values)
# 
# # 走訪第一層index，"Industry"
# with pd.ExcelWriter("需求1_行業別客戶別排序.xlsx",mode = "w") as writer:
#     for i in unique_values:
#         sheet_name = str(i)
#         temp = result.loc[i]
#         temp = temp.sort_values(ascending = False) 
#     
#         temp_len_20 = int( len(temp) * 0.2 )
#         temp = temp.iloc[:temp_len_20]
#         
#         temp.to_excel(writer, sheet_name = sheet_name)
# 
# 
# =============================================================================
