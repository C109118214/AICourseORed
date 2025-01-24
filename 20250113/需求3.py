# -*- coding: utf-8 -*-
import pandas as pd

# 讀取資料
Data_path = "零售資料/"
Item_df = pd.read_csv(f"{Data_path}貨品資料.csv")
Salesperson_df = pd.read_csv(f"{Data_path}貨品資料.csv")
Customer_df = pd.read_csv(f"{Data_path}客戶資料.csv")
Fact_df = pd.read_csv(f"{Data_path}銷貨資料_fact_table.csv")


# 將銷售資料與客戶的資料合併，以便根據產業分組
Industry_df = pd.merge(left = Fact_df,
                       right = Customer_df,
                       left_on = "Customer_ID",
                       right_on = "Customer_ID"
                       )
# 需求3，分產業別、客戶每個月總銷售額整理
 

# 銷售額
Industry_df["Sales_Amount"] = Industry_df["Quantity"] * Industry_df["Unit_price"]
Industry_df["Year_month"] = pd.to_datetime(Industry_df["Date"]).dt.strftime('%Y%m')

#Industry_group = Industry_df.groupby(by = ["Industry", "Year_month", "Customer_ID"])

# 產業列表與年月列表
Industry_list = Industry_df["Industry"].unique()
Year_month_list = Industry_df["Year_month"].unique()
Year_month_list.sort()

with pd.ExcelWriter("需求3_分產業別、客戶每個月總銷售額整理.xlsx",mode = "w") as writer:
    for ind in Industry_list:
        ind_sum_df = pd.DataFrame(index = Year_month_list)
        ind_df = Industry_df[ Industry_df["Industry"] == ind ]
        ind_group_sum = ind_df.groupby(by = ["Year_month", "Customer_ID"])["Sales_Amount"].sum()
        
        # 將加總的資料填入DataFrame
        for i in ind_group_sum.index:
            ym, cus_id = i
            ind_sum_df.at[ym, cus_id] = ind_group_sum[i]
        ind_sum_df = ind_sum_df.dropna(how = "all").fillna(0)
        ind_sum_df.to_excel(writer, sheet_name = ind)
