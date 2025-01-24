# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 10:46:21 2022

@author: user
"""
import pandas as pd
from plotly.graph_objs import Figure

df = pd.read_excel("data_df.xlsx") #讀取資料
df2 = pd.read_excel("record_df.xlsx") # 讀取交易紀錄

df_Buy = df2[ df2["LS"] == "L"] # 買入點資料
df_Sell = df2[ df2.LS == "S"] # 賣出點資料

trace_1 = {
    "type" : "candlestick", # 設定圖表種類為K線圖(蠟燭圖)
    "x" : df["日期"],
    "open" : df["開盤價"],
    "high" : df["最高價"],
    "low" : df["最低價"],
    "close" : df["收盤價"],
    "name" : "K線",
    "increasing_line_color" : "red", # 設定上漲為紅
    "decreasing_line_color" : "green" # 設定下跌為綠
    }

trace_2 = {
    "type" : "scatter",
    "x" : df_Buy["time"],
    "y" : df_Buy["price"],
    "name" : "買入點",
    "mode" : "markers", # 點圖標記
    "marker" : {
        "size" : 10,
        "color" : "blue"
        }
    }

trace_3 = {
    "type" : "scatter",
    "x" : df_Sell["time"],
    "y" : df_Sell["price"],
    "name" : "賣出點",
    "mode" : "markers", # 點圖標記
    "marker" : {
        "symbol" : "diamond",
        "size" : 10,
        "color" : "black"
        }
    }

trace_4 = {
    "type" : "scatter",
    "x" : df["日期"],
    "y" : df["upper"],
    "name" : "上布林線",
    "mode" : "lines", # 線圖
    "marker" : {
        "color" : "orange"
        }
    }

trace_5 = {
    "type" : "scatter",
    "x" : df["日期"],
    "y" : df["MA"],
    "name" : "中線",
    "mode" : "lines", # 線圖
    "marker" : {
        "color" : "yellow"
        }
    }

trace_6 = {
    "type" : "scatter",
    "x" : df["日期"],
    "y" : df["lower"],
    "name" : "下布林線",
    "mode" : "lines", # 線圖
    "marker" : {
        "color" : "purple"
        }
    }

layout = {
    "title" : "布林通道買賣點",
    "xaxis" : {"title" : "日期"},
    "yaxis" : {"title" : "價格"}
    }

# 將圖的設定放到串列中
data = [ trace_1, trace_2, trace_3, trace_4, trace_5, trace_6 ]

# 繪圖
fig = Figure(data = data, layout = layout)

fig_html = fig.to_html() # 將繪圖轉換成HTML碼

# 儲存HTML碼，並且指定為UTF8編碼
with open("BBAND.html", "w+", encoding = "UTF8") as f:
    f.write(fig_html)

