# -*- coding: utf-8 -*-
import requests

url = "https://www.twse.com.tw/rwd/zh/afterTrading/STOCK_DAY?date=20250101&stockNo=1101&response=json&_=1736755383494"

res = requests.get(url)
print(res.text)