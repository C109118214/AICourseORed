import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df = pd.read_excel("技術指標.xlsx")
df["日期"] = pd.to_datetime(df["日期"])  # 確保日期格式

# 建立子圖：K 線圖與 MACD 圖
fig = make_subplots(
    rows=2, cols=1,  # 兩個子圖
    shared_xaxes=True,  # 共用 X 軸
    vertical_spacing=0.1,  # 子圖間的間距
    row_heights=[0.7, 0.3]  # 調整子圖高度比例
)

# 添加 K 線圖
fig.add_trace(
    go.Candlestick(
        x=df["日期"],
        open=df["開盤價"],
        high=df["最高價"],
        low=df["最低價"],
        close=df["收盤價"],
        increasing_line_color='red',  # 漲：紅色
        decreasing_line_color='green',  # 跌：綠色
        name="K 線圖"
        
    ),
    row=1, col=1
)

# 添加 MACD 線
fig.add_trace(
    go.Scatter(
        x=df["日期"],
        y=df["MACD"],
        mode="lines",
        name="MACD",
        line=dict(color="blue")
    ),
    row=2, col=1
)

# 添加 MACD Signal 線
fig.add_trace(
    go.Scatter(
        x=df["日期"],
        y=df["MACD_Signal"],
        mode="lines",
        name="MACD Signal",
        line=dict(color="orange")
    ),
    row=2, col=1
)

# 添加 MACD Histogram
fig.add_trace(
    go.Bar(
        x=df["日期"],
        y=df["MACD_Hist"],
        name="MACD Histogram",
        marker_color="purple"
    ),
    row=2, col=1
)

# 更新圖表外觀
fig.update_layout(
    title="K 線圖與 MACD 指標",
    xaxis_rangeslider_visible=False,  # 隱藏範圍滑動條
    xaxis2_title="日期",  # 設定 X 軸標題
    yaxis_title="價格",  # 第一圖 Y 軸
    yaxis2_title="MACD",  # 第二圖 Y 軸
    #height=600  # 調整總圖表高度
)
fig_html = fig.to_html() # 將繪圖轉換成HTML碼

# 儲存HTML碼，並且指定為UTF8編碼
with open("MACD.html", "w+", encoding = "UTF8") as f:
    f.write(fig_html)