## on draw_plot
```python
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
```

## on ui
```python
def onclick(self):
        stock_id = self.lineEdit.text()  # 獲取用戶輸入的幣種代號
        df = dp(stock_id, "1h", 30)  # 調用主函數
        if df is None:
            self.label_2.setText("無效的幣種代號或無法獲取資料")
            self.label.setPixmap(QtGui.QPixmap("起始圖.png"))
            self.tableWidget.clear()
            return
        self.label.setPixmap(QtGui.QPixmap(f"{stock_id}_Kbar.png"))
```
![image](https://github.com/user-attachments/assets/5af1e23c-481a-42cb-b7f9-145ad8bf326d)
