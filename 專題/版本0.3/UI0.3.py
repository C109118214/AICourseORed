import sys
from PyQt5 import QtWidgets, QtWebEngineWidgets
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QComboBox
from binance.client import Client
import pandas as pd
import plotly.graph_objs as go
import talib

# 初始化 Binance API（請輸入你的 API 金鑰）
#client = Client(api_key="", api_secret="")

client = Client()

class BinanceApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Binance 仿交易界面")
        self.setGeometry(100, 100, 1200, 800)
        self.initUI()

    def initUI(self):
        # 主布局
        main_layout = QHBoxLayout()

        # 左側圖表區域
        self.chart_view = QtWebEngineWidgets.QWebEngineView()
        self.chart_view.setMinimumWidth(800)

        # 右側功能區域
        right_layout = QVBoxLayout()

        # 輸入與加載區
        self.symbol_input = QLineEdit(self)
        self.symbol_input.setPlaceholderText("輸入幣種對（如 BTCUSDT）")
        self.load_button = QPushButton("加載數據", self)
        self.load_button.clicked.connect(self.load_data)

        interval_label = QLabel("選擇時間間隔：", self)
        self.interval_combo = QComboBox(self)
        self.interval_combo.addItems(["1m", "5m", "15m", "30m", "1h", "4h", "1d"])

        right_layout.addWidget(self.symbol_input)
        right_layout.addWidget(interval_label)
        right_layout.addWidget(self.interval_combo)
        right_layout.addWidget(self.load_button)

        # 技術指標按鈕
        self.ma5_button = QPushButton("顯示 MA5", self)
        self.ma5_button.clicked.connect(self.plot_ma5)
        self.ma10_button = QPushButton("顯示 MA10", self)
        self.ma10_button.clicked.connect(self.plot_ma10)
        self.rsi_button = QPushButton("顯示 RSI", self)
        self.rsi_button.clicked.connect(self.plot_rsi)
        self.macd_button = QPushButton("顯示 MACD", self)
        self.macd_button.clicked.connect(self.plot_macd)

        right_layout.addWidget(self.ma5_button)
        right_layout.addWidget(self.ma10_button)
        right_layout.addWidget(self.rsi_button)
        right_layout.addWidget(self.macd_button)

        # 訂單簿區域
        self.order_book_table = QTableWidget(10, 3)
        self.order_book_table.setHorizontalHeaderLabels(["價格", "數量", "類型"])
        right_layout.addWidget(QLabel("訂單簿：", self))
        right_layout.addWidget(self.order_book_table)

        # 主界面佈局整合
        main_layout.addWidget(self.chart_view)
        main_layout.addLayout(right_layout)

        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def load_data(self):
        symbol = self.symbol_input.text()
        interval = self.interval_combo.currentText()
        try:
            klines = client.get_historical_klines(symbol, interval, "1 day ago UTC")
            self.df = pd.DataFrame(klines, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time',
                                                    'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume',
                                                    'taker_buy_quote_asset_volume', 'ignore'])
            self.df['timestamp'] = pd.to_datetime(self.df['timestamp'], unit='ms')
            self.df.set_index('timestamp', inplace=True)
            self.df[['open', 'high', 'low', 'close', 'volume']] = self.df[['open', 'high', 'low', 'close', 'volume']].astype(float)
            self.plot_candlestick()
        except Exception as e:
            print(f"Error loading data: {e}")

    def plot_candlestick(self):
        fig = go.Figure(data=[go.Candlestick(x=self.df.index,
                                             open=self.df['open'],
                                             high=self.df['high'],
                                             low=self.df['low'],
                                             close=self.df['close'])])
        self.chart_view.setHtml(fig.to_html(include_plotlyjs='cdn'))

    def plot_ma5(self):
        self.df['MA5'] = talib.SMA(self.df['close'], timeperiod=5)
        fig = go.Figure(data=[go.Candlestick(x=self.df.index,
                                             open=self.df['open'],
                                             high=self.df['high'],
                                             low=self.df['low'],
                                             close=self.df['close']),
                              go.Scatter(x=self.df.index, y=self.df['MA5'], mode='lines', name='MA5')])
        self.chart_view.setHtml(fig.to_html(include_plotlyjs='cdn'))

    def plot_ma10(self):
        self.df['MA10'] = talib.SMA(self.df['close'], timeperiod=10)
        fig = go.Figure(data=[go.Candlestick(x=self.df.index,
                                             open=self.df['open'],
                                             high=self.df['high'],
                                             low=self.df['low'],
                                             close=self.df['close']),
                              go.Scatter(x=self.df.index, y=self.df['MA10'], mode='lines', name='MA10')])
        self.chart_view.setHtml(fig.to_html(include_plotlyjs='cdn'))

    def plot_rsi(self):
        self.df['RSI'] = talib.RSI(self.df['close'], timeperiod=14)
        fig = go.Figure(data=[go.Scatter(x=self.df.index, y=self.df['RSI'], mode='lines', name='RSI')])
        self.chart_view.setHtml(fig.to_html(include_plotlyjs='cdn'))

    def plot_macd(self):
        macd, macd_signal, macd_hist = talib.MACD(self.df['close'], fastperiod=12, slowperiod=26, signalperiod=9)
        fig = go.Figure(data=[
            go.Scatter(x=self.df.index, y=macd, mode='lines', name='MACD'),
            go.Scatter(x=self.df.index, y=macd_signal, mode='lines', name='Signal'),
            go.Bar(x=self.df.index, y=macd_hist, name='Histogram')
        ])
        self.chart_view.setHtml(fig.to_html(include_plotlyjs='cdn'))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = BinanceApp()
    window.show()
    sys.exit(app.exec_())
