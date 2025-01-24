# -*- coding: utf-8 -*-
import requests
import pandas as pd

post_data = {
    "encodeURIComponent" : 1,
    "step" : 1,
    "firstin" : 1,
    "off" : 1,
    "isQuery" : "Y",
    "TYPEK" : "sii",
    "year" : 113,
    "season" : 3
    }

url = "https://mops.twse.com.tw/mops/web/ajax_t163sb04"

res = requests.post(url , data = post_data )

df_list = pd.read_html(res.text)
