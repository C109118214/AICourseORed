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

# 銷售額
Industry_df["Sales_Amount"] = Industry_df["Quantity"] * Industry_df["Unit_price"]
# 年月分組依據
Industry_df["Year_month"] = pd.to_datetime(Industry_df["Date"]).dt.strftime('%Y%m')

Industry_group = Industry_df.groupby(by = ["Industry", "Year_month"])

YM_group_sales_sum = Industry_group["Sales_Amount"].sum()
YM_group_customer_count = Industry_group["Customer_ID"].nunique() # 計算每一組的不重複客戶數量
YM_group_order_count = Industry_group["Sales_Amount"].count() # 計算每一組的訂單數

Customer_mean_YM = YM_group_sales_sum / YM_group_customer_count
order_mean_YM = YM_group_sales_sum / YM_group_order_count

with pd.ExcelWriter("需求2_客單價、筆單價.xlsx",mode = "w") as writer:
    Customer_mean_YM.to_excel(writer, sheet_name = "客單價")
    order_mean_YM.to_excel(writer, sheet_name = "筆單價")

