# -*- coding: utf-8 -*-
import pandas as pd

path = "資料/"
df_sell = pd.read_excel(f"{path}銷售資料.xlsx")
df_good = pd.read_excel(f"{path}商品資料.xlsx")

df = pd.merge(left = df_sell,
              right = df_good,
              left_on = "貨品編號",
              right_on = "貨品編號"
              )

# 假設df_good中沒有A
df_good_non_A = df_good[df_good["貨品編號"] != "A"]
# 預設為內部合併，兩邊有資料沒有對上，就不會被合併進來
# 只剩下875筆資料
df_2 = pd.merge(left = df_sell,
              right = df_good_non_A,
              left_on = "貨品編號",
              right_on = "貨品編號"
              )

# 以左邊的資料為準，沒有對應上的，還是保留
df_3 = pd.merge(left = df_sell,
              right = df_good_non_A,
              left_on = "貨品編號",
              right_on = "貨品編號",
              how = "left"
              )

# 以右邊的資料為準，沒有對應上的，還是保留
df_4 = pd.merge(left = df_sell,
              right = df_good_non_A,
              left_on = "貨品編號",
              right_on = "貨品編號",
              how = "right"
              )

# 以兩邊沒有對應上的都保留
df_5 = pd.merge(left = df_sell,
              right = df_good_non_A,
              left_on = "貨品編號",
              right_on = "貨品編號",
              how = "outer"
              )

