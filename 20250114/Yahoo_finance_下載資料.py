import yfinance as yf

# 設定目標股票代碼（例如 AAPL）
#ticker = "NQ=F" # 股票代號從Yahoo Finance網站上找尋
ticker = "2330.tw"

# 下載歷史資料
data = yf.download(ticker, start="2010-01-01",
                   end="2023-12-31",
                   interval="1d")

# 查看資料
print(data.head())

# 儲存為 CSV
data.to_csv(f"{ticker}_historical_data.csv")
print(f"{ticker} 歷史資料已儲存至 {ticker}_historical_data.csv")
