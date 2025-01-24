
def plot_indicator(self, indicator):
        fig = go.Figure()
        ma_period = int(self.ma_combo.currentText()[3:])
        
        if indicator == "EMA":
            self.df['EMA'] = talib.EMA(self.df['close'], timeperiod=ma_period)
            fig.add_trace(go.Scatter(x=self.df.index, y=self.df['EMA'], mode='lines', name='EMA'))

        elif indicator == "RSI":
            self.df['RSI'] = talib.RSI(self.df['close'], timeperiod=14)
            fig.add_trace(go.Scatter(x=self.df.index, y=self.df['RSI'], mode='lines', name='RSI'))

        elif indicator == "MACD":
            macd, macd_signal, macd_hist = talib.MACD(self.df['close'], fastperiod=12, slowperiod=26, signalperiod=9)
            fig.add_trace(go.Scatter(x=self.df.index, y=macd, mode='lines', name='MACD'))
            fig.add_trace(go.Scatter(x=self.df.index, y=macd_signal, mode='lines', name='Signal'))
            fig.add_trace(go.Bar(x=self.df.index, y=macd_hist, name='Histogram'))

        elif indicator == "Bollinger Bands":
            upper, middle, lower = talib.BBANDS(self.df['close'], timeperiod=20, nbdevup=2, nbdevdn=2, matype=0)
            fig.add_trace(go.Scatter(x=self.df.index, y=upper, mode='lines', name='Upper Band'))
            fig.add_trace(go.Scatter(x=self.df.index, y=middle, mode='lines', name='Middle Band'))
            fig.add_trace(go.Scatter(x=self.df.index, y=lower, mode='lines', name='Lower Band'))

        elif indicator == "ADX":
            self.df['ADX_14'] = talib.ADX(self.df['high'], self.df['low'], self.df['close'], timeperiod=14)
            fig.add_trace(go.Scatter(x=self.df.index, y=self.df['ADX_14'], mode='lines', name='ADX'))

        elif indicator == "ATR":
            self.df['ATR_14'] = talib.ATR(self.df['high'], self.df['low'], self.df['close'], timeperiod=14)
            fig.add_trace(go.Scatter(x=self.df.index, y=self.df['ATR_14'], mode='lines', name='ATR'))

        elif indicator == "CCI":
            self.df['CCI_20'] = talib.CCI(self.df['high'], self.df['low'], self.df['close'], timeperiod=20)
            fig.add_trace(go.Scatter(x=self.df.index, y=self.df['CCI_20'], mode='lines', name='CCI'))

        elif indicator == "Stochastic":
            self.df['SlowK'], self.df['SlowD'] = talib.STOCH(self.df['high'], self.df['low'], self.df['close'],
                                                         fastk_period=14, slowk_period=3, slowk_matype=0,
                                                         slowd_period=3, slowd_matype=0)
            fig.add_trace(go.Scatter(x=self.df.index, y=self.df['SlowK'], mode='lines', name='SlowK'))
            fig.add_trace(go.Scatter(x=self.df.index, y=self.df['SlowD'], mode='lines', name='SlowD'))

        elif indicator == "SAR":
            self.df['SAR'] = talib.SAR(self.df['high'], self.df['low'], acceleration=0.02, maximum=0.2)
            fig.add_trace(go.Scatter(x=self.df.index, y=self.df['SAR'], mode='lines', name='SAR'))


        # 更新圖表
        self.chart_view.setHtml(fig.to_html(include_plotlyjs='cdn'))
