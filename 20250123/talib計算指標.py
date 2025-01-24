# -*- coding: utf-8 -*-
import talib
import pandas as pd

data_path = "股價資料彙整/"
stock_id = "1101"
df = pd.read_excel(f"{data_path}{stock_id}.xlsx")

# 如果開高低收有任一個是空值，刪除該筆資料
df = df.dropna(subset = ["開盤價", "最高價", "最低價", "收盤價"])
# 刪除漲跌價差欄位，因為可能有空值會影響到後續的dropna
df = df.drop(["漲跌價差"], axis = 1)
# 計算五日均線
df["MA5"] = talib.SMA(df["收盤價"], 5)

df["MA10"] = talib.SMA(df["收盤價"], 10)


# 確保 '收盤價' 欄位存在
close_prices = df['收盤價']

# 1. 移動平均線 (MA)
df['MA20'] = talib.SMA(close_prices, timeperiod=20)

# 2. 指數移動平均線 (EMA)
df['EMA_20'] = talib.EMA(close_prices, timeperiod=20)

# 3. 相對強弱指數 (RSI)
df['RSI_14'] = talib.RSI(close_prices, timeperiod=14)

# 4. 指數平滑異同移動平均線 (MACD)
df['MACD'], df['MACD_Signal'], df['MACD_Hist'] = talib.MACD(close_prices, 
                                                             fastperiod=12, 
                                                             slowperiod=26, 
                                                             signalperiod=9)

# 5. 布林通道 (Bollinger Bands)
df['BB_Upper'], df['BB_Middle'], df['BB_Lower'] = talib.BBANDS(close_prices, 
                                                                timeperiod=20, 
                                                                nbdevup=2, 
                                                                nbdevdn=2, 
                                                                matype=0)

# 6. 平均方向指數 (ADX)
df['ADX_14'] = talib.ADX(df['最高價'], df['最低價'], close_prices, timeperiod=14)

# 7. 平均真實波幅 (ATR)
df['ATR_14'] = talib.ATR(df['最高價'], df['最低價'], close_prices, timeperiod=14)

# 8. 商品通道指數 (CCI)
df['CCI_20'] = talib.CCI(df['最高價'], df['最低價'], close_prices, timeperiod=20)

# 9. 隨機指標 (Stochastic Oscillator)
df['SlowK'], df['SlowD'] = talib.STOCH(df['最高價'], 
                                       df['最低價'], 
                                       close_prices, 
                                       fastk_period=14, 
                                       slowk_period=3, 
                                       slowk_matype=0, 
                                       slowd_period=3, 
                                       slowd_matype=0)

# 10. 拋物線轉向指標 (SAR)
df['SAR'] = talib.SAR(df['最高價'], df['最低價'], acceleration=0.02, maximum=0.2)

# 預測目標，N天後有沒有上漲
N = 10
df["Close_T+N"] = df['收盤價'].shift(-N) > df['收盤價']
# 以隔日的開盤價買入
df["買入價格"] = df["開盤價"].shift(-1)
# 假設買入後持有五天賣出，每股獲利金額
# 手續費、證交稅視為賣出的減項，買入的加項
df["Profit"] = df['收盤價'].shift(-N)  * (1 - 0.001425 * 0.5 - 0.003) - df["買入價格"] * (1 + 0.001425 * 0.5)

# 只要有空值，就刪除該筆資料
df = df.dropna()

df["MA5_10"] = df["MA5"] > df["MA10"]
df["MA10_20"] = df["MA10"] > df["MA20"]
df["over_MA5"] = df["收盤價"] > df["MA5"]
df["over_MA10 "] = df["收盤價"] > df["MA10"]
df["over_MA20"] = df["收盤價"] > df["MA20"]
df["EMA_20_over"] = df["收盤價"] > df['EMA_20']
df["RSI_30"] = df["RSI_14"] < 30 
df["RSI_70"] = df["RSI_14"] > 70
df["MACD_Hist_pos"] = df["MACD_Hist"] > 0
df["BBAND_over_upper"] = df["收盤價"] > df['BB_Upper']
df["BBAND_under_lower"] = df["收盤價"] < df['BB_Lower']
df["K_80"] = df['SlowK'] > 80
df["K_20"] = df['SlowK'] < 20
df["K_over_D"] = df['SlowK'] > df['SlowD']
df["ADX_25"] = df["ADX_14"] > 25
df["ADX_20"] = df["ADX_14"] < 20
df["over_ATR"] = df["收盤價"] > df["ATR_14"]
df["CCI_100"] = df["CCI_20"] > 100
df["CCI_-100"] = df["CCI_20"] < -100
df["over_SAR"] = df["收盤價"] > df['SAR']
# 檢查結果

# 保存數據
df.to_excel('技術指標.xlsx', index=False)
