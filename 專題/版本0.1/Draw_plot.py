# =============================================================================
# # -*- coding: utf-8 -*-
# import pandas as pd
# import mplfinance as fplt
# import yfinance as yf
# from binance import Client
# def main(stock_id):
#     # 下載近30天的資料
#     df = yf.download(stock_id, period = "1mo",
#                        interval="1d")
#     df.columns = df.columns.get_level_values(0)
#     print(df.columns)
#     # 調整圖表標示顏色
#     mc = fplt.make_marketcolors(
#                                 up = 'tab:red',down = 'tab:green', # 上漲為紅，下跌為綠
#                                 wick = {'up':'red','down':'green'}, # 影線上漲為紅，下跌為綠
#                                 volume = 'tab:blue', # 交易量顏色
#                                )
#     
#     # 定義圖表風格
#     s = fplt.make_mpf_style(marketcolors = mc,
#                             rc = {
#                                 'font.size': 10, #文字大小
#                                 "font.family":['sans-serif', "Microsoft JhengHei"] # 字型
#                             }
#                         ) 
#     
#     fplt.plot(
#                 df, # 開高低收量的資料
#                 type = 'candle', # 類型為蠟燭圖，也就是 K 線圖
#                 style = s, # 套用圖表風格
#                 title = stock_id, # 設定圖表標題
#                 ylabel = '價格', # 設定 Y 軸標題
#                 volume = True,
#                 savefig='stock_Kbar.png', # 儲存檔案
#             )
#     return df.round(2)
#     
# # 當這支程式被直接執行的時候，會執行測試的程式碼main("AAPL")
# # 被匯入(import)的時候__name__就會變成檔案名稱Draw_plot，
# # 就不會執行main("AAPL")
# if __name__ == "__main__":
# 
#     main("2330.tw")
# =============================================================================
# -*- coding: utf-8 -*-
"""
Updated on Fri Jan 24 14:47:14 2025

@Updated by: USER
"""

import pandas as pd
import mplfinance as fplt
from binance import Client

def main(stock_id, interval="1h", days=30):
    """
    Main function to fetch Binance data and plot K-line chart.
    :param stock_id: Cryptocurrency pair (e.g., "BTCUSDT").
    :param interval: K-line interval (e.g., "1m", "1h", "1d").
    :param days: Number of days to fetch data for.
    :return: DataFrame containing OHLC and volume data.
    """
    try:
        # Initialize Binance Client
        client = Client()
        
        # Fetch historical K-line data
        klines = client.get_historical_klines(stock_id, interval, f"{days} day ago UTC")
        df_columns = [
            "Open_time", "Open", "High", "Low", "Close", "Volume",
            "Close_time", "Quote_asset_volume", "Number_of_trades",
            "Taker_buy_base_asset_volume", "Taker_buy_quote_asset_volume", "Ignore"
        ]
        df = pd.DataFrame.from_records(klines, columns=df_columns)
        
        # Convert timestamps and format DataFrame
        df["Open_time"] = pd.to_datetime(df["Open_time"], unit="ms")
        df.set_index("Open_time", inplace=True)
        df = df[["Open", "High", "Low", "Close", "Volume"]].astype(float)

        # Customize chart appearance
        mc = fplt.make_marketcolors(
            up="tab:red", down="tab:green",
            wick={"up": "red", "down": "green"},
            volume="tab:blue"
        )
        s = fplt.make_mpf_style(marketcolors=mc, rc={"font.size": 10, "font.family": ["sans-serif", "Microsoft JhengHei"]})

        # Plot K-line chart
        fplt.plot(
            df,
            type="candle",
            style=s,
            title=f"{stock_id} {interval} Chart",
            ylabel="Price",
            volume=True,
            savefig=f"{stock_id}_Kbar.png"
        )
        print(f"K-line chart saved as {stock_id}_Kbar.png")
        return df.round(2)

    except Exception as e:
        print(f"Error: {e}")
        return None

# Test the function
if __name__ == "__main__":
    main("BTCUSDT", "1h", 30)