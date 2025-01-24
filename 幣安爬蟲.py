# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 14:32:20 2025

@author: USER
"""

from binance import Client
import pandas as pd

client = Client()

N_days = 30


# 下載資料
klines = client.get_historical_klines("TRUMPUSDT", Client.KLINE_INTERVAL_1HOUR, f"{N_days} day ago UTC")
df = pd.DataFrame.from_records(klines)
df_columns = ["Open_time", "Open", "High", "Low", "Close", "Volumn", "Close_time", "Quote_asset_volume", "Number_of_trades", "Taker_buy_base_asset_volume", "Taker_buy_quote_asset_volume", "Ignore"]
df.columns = df_columns
df["Open_time"] = pd.to_datetime(df["Open_time"] * 1000000) #*1000000變成正常時間


#df.to_csv("BTCUSDT_1DAY.csv", index = False)