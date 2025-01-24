import pandas as pd
import plotly.graph_objects as go

df = pd.read_excel("技術指標.xlsx")

df["日期"] = pd.to_datetime(df["日期"])  # 確保日期格式

# 建立子圖：K 線圖與 MACD 圖
fig = go.Figure()

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
)

# 更新圖表外觀

# 啟用範圍滑動條並讓 Y 軸自動縮放
fig.update_layout(
    title="自動縮放 Y 軸的 K 線圖",
    xaxis_title="日期",
    yaxis_title="價格",
    xaxis_rangeslider_visible=True,  # 顯示範圍滑動條
    yaxis=dict(
        autorange=True,  # 啟用自動調整
        fixedrange=False  # 允許縮放
    ),
    height=600
)


fig_html = fig.to_html() # 將繪圖轉換成HTML碼

# 儲存HTML碼，並且指定為UTF8編碼
with open("K_line.html", "w+", encoding = "UTF8") as f:
    f.write(fig_html)