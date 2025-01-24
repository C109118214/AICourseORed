# -*- coding: utf-8 -*-
import talib
import pandas as pd
import numpy as np
from os import listdir
from tqdm import tqdm

# 關閉未來語法警告，不然一直print煩死
pd.set_option('future.no_silent_downcasting', True)

data_path = "股價資料彙整/"
data_list =  listdir(data_path)

def main(file_name):
    df = pd.read_excel(f"{data_path}{file_name}")
    # 有可能有收盤價等於0的
    df = df[df["收盤價"] > 0]
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
    
    
    
    # 以隔日的開盤價買入
    df["買入價格"] = df["開盤價"].shift(-1)
    # 預測目標，N天後有沒有上漲
    N = 60
    df["Close_T+N"] = np.log( df['收盤價'].shift(-N) / df["買入價格"] )
    
    # 只要有空值，就刪除該筆資料
    df = df.dropna()
    
    df["MA5_10"] = df["MA5"] > df["MA10"]
    df["MA10_20"] = df["MA10"] > df["MA20"]
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
    # 將日期以外的數值轉換成浮點數，節省除儲存空間
    df.replace({True: 1, False: 0}, inplace = True)
    df = df.round(4)  # 四捨五入到小數點第4位
    return df

df_list = [] # 存放處理好的df，以便最後合併
for file_name in tqdm(data_list):
    df = main(file_name)
    #去除副檔名，就是股票代號
    stock_id = file_name.replace(".xlsx", "")
    # 將股票代號指派給df
    df["股票代號"] = stock_id
    # 將df新增進df_list
    df_list.append(df)
# 將所有的DF合併
result_df = pd.concat(df_list)
# 資料可能會超出EXCEL的限制，所以存成CSV
result_df.to_csv("所有股票技術指標.csv", index = False)