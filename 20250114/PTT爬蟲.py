# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.ptt.cc/bbs/stock/index.html"

res = requests.get(url)
#HTML程式碼解析
soup = BeautifulSoup(res.text, features="lxml")

all_article = soup.select("div.r-ent")
data_list = []
for article in all_article:
    title_obj = article.select("div.title a")[0]
    href = title_obj.get("href")
    title = title_obj.text
    people = article.select("div.nrec")[0].text
    author = article.select("div.author")[0].text
    date = article.select("div.date")[0].text
    data_dict = {
        "標題" : title,
        "網址" : href,
        "人氣" : people,
        "作者" : author,
        "日期" : date
        }
    data_list.append(data_dict)

df = pd.DataFrame(data_list)
df.to_excel("PTT結果.xlsx", index = False)
# =============================================================================
#     print(title_obj.get("href"))
#     print(title_obj.text)
#     print(people )
#     print(author )
#     print(date)
# =============================================================================
