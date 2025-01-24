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

df.plot(kind = "scatter",
        x = "開盤價",
        y = "收盤價"
        )

plt.title('漲跌與否比例') # 圖表標題
plt.show() # 顯示圖片
