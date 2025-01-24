# -*- coding: utf-8 -*-
import requests
import json
import pandas as pd
url = "https://www.twse.com.tw/rwd/zh/afterTrading/STOCK_DAY?date=20250101&stockNo=1101&response=json&_=1736755383494"

res = requests.get(url)
print(res.text)

stock_data = json.loads(res.text)
df = pd.DataFrame.from_records(stock_data["data"])
df.columns = stock_data["fields"]
df.to_excel("股價資料/1101_202501.xlsx", index = False)
print(df)