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

# 繪圖
df.plot(kind = "barh", # 圖形類別
        x = "日期", # X軸設定
        y = '漲跌價差' # Y軸設定
        )

plt.title('漲跌價差') # 圖表標題
plt.xlabel('日期') # X軸標籤
plt.ylabel('漲跌幅') # Y軸標籤
plt.show() # 顯示圖片
