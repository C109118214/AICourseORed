import pandas as pd
import mplfinance as fplt
import yfinance as yf

def main(stock_id):
    # 下載近30天的資料
    df = yf.download(stock_id, period = "1mo",
                       interval="1d")
    df.columns = df.columns.get_level_values(0)
    print(df.columns)
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
                title = stock_id, # 設定圖表標題
                ylabel = '價格', # 設定 Y 軸標題
                volume = True,
                savefig='stock_Kbar.png', # 儲存檔案
            )
    
# 當這支程式被直接執行的時候，會執行測試的程式碼main("AAPL")
# 被匯入(import)的時候__name__就會變成檔案名稱Draw_plot，
# 就不會執行main("AAPL")
if __name__ == "__main__":

    main("GOOG")