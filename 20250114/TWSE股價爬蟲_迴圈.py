# -*- coding: utf-8 -*-
import requests
import json
import pandas as pd
import time

def main( stock_id, year_month ):
    url = f"https://www.twse.com.tw/rwd/zh/afterTrading/STOCK_DAY?date={year_month}01&stockNo={stock_id}&response=json&_=1736755383494"
    
    res = requests.get(url)
    
    stock_data = json.loads(res.text)
    df = pd.DataFrame.from_records(stock_data["data"])
    df.columns = stock_data["fields"]
    df.to_excel(f"股價資料/{stock_id}_{year_month}.xlsx", index = False)

stock_list = [1101, 2330, 2603, 1234, 2498]
date_list = []
for y in range(2022, 2024+1):
    for m in range(1, 12+1):
        date_list.append(y*100 + m)
print(date_list )

for s_id in stock_list:
    for ym in date_list:
        main(s_id, ym)
        time.sleep(5) # 每次抓取後休息五秒
#main(2330, 202406)