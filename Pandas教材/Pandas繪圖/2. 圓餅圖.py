# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

# 設定繪圖的參數
plt.rcParams.update({
    'font.size': 10, #文字大小
    "font.family":['sans-serif', "Microsoft JhengHei"] # 字型
})
# 'sans-serif'為英文字體，不加入的話負號會顯示不出來
# 微軟正黑體 Microsoft JhengHei
# 標楷體 DFKai-SB

df = pd.read_excel( "0050.xlsx" ) # 讀取資料
df["日期"] = pd.to_datetime(df["日期"]) # 將文字轉datetime格式

#df["日期"] = df["日期"].dt.date # 只保留日期
df["日期"] = df["日期"].dt.strftime('%m-%d') # 只保留月與日

df.index = df["日期"] # 將索引換成日期，以便繪圖時被設定為X軸的標籤

# 統計漲跌
df["漲跌與否"] = df["漲跌價差"] > 0 # 判斷是否有上漲
df_group = df.groupby(by = ['漲跌與否']) # 根據是否有上漲進行分組
df_rise_count = df_group.count() # 將各組進行數量計算

print(df_rise_count) # 會將每一欄進行統計
df_rise_count.to_excel("123.xlsx")
print(df_rise_count['日期'])  # 因為數值都一樣，所以抓其中一欄進行繪圖即可

# 進行圓餅圖繪圖
df_rise_count['日期'].plot(kind = "pie")

plt.title('漲跌與否比例') # 圖表標題
plt.ylabel('漲跌與否比例') # Y軸標籤
plt.show() # 顯示圖片
