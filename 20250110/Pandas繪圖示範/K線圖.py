# -*- coding: utf-8 -*-
import mplfinance as fplt
import pandas as pd

df = pd.read_excel("0050.xlsx")
df["日期"] = pd.to_datetime(df["日期"])
df.index = df["日期"]
# 重新命名欄位，以符合fplt的格式
df.rename(columns = {"開盤價" : "Open",
                "最高價" : "High",
                "最低價" : "Low",
                "收盤價" : "Close",
                "成交股數" : "Volume"
                }, inplace = True)
# 調整圖表標示顏色
mc = fplt.make_marketcolors(
                            up = 'tab:red',down = 'tab:green', # 上漲為紅，下跌為綠
                            wick = {'up':'red','down':'green'}, # 影線上漲為紅，下跌為綠
                            volume = 'tab:blue', # 交易量顏色
                           )

# 定義圖表風格
s = fplt.make_mpf_style(marketcolors = mc,
                        rc = {
                            'font.size': 10, #文字大小
                            "font.family":['sans-serif', "Microsoft JhengHei"] # 字型
                        }
                    ) 

fplt.plot(
            df, # 開高低收量的資料
            type = 'candle', # 類型為蠟燭圖，也就是 K 線圖
            style = s, # 套用圖表風格
            title = "0050", # 設定圖表標題
            ylabel = '價格', # 設定 Y 軸標題
            volume = True,
            savefig='K線圖/stock_Kbar.png', # 儲存檔案
        )
