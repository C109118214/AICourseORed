# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from tqdm import tqdm
from xgboost import XGBRegressor
from sklearn.preprocessing import StandardScaler
df = pd.read_csv("所有股票技術指標.csv")
df = df[df["收盤價"] > 0]

scaler = StandardScaler()
Z_score_columns = ['成交股數', '成交金額', '開盤價', '最高價', '最低價', '收盤價', '成交筆數', 'MA5', 'MA10',
       'MA20', 'EMA_20', 'RSI_14', 'MACD', 'MACD_Signal', 'MACD_Hist',
       'BB_Upper', 'BB_Middle', 'BB_Lower', 'ADX_14', 'ATR_14', 'CCI_20',
       'SlowK', 'SlowD', 'SAR']

scaler.fit(df[Z_score_columns])
df[Z_score_columns] = scaler.transform(df[Z_score_columns])

df["日期"] = pd.to_datetime(df["日期"])
df["季別"] = df["日期"].dt.year * 100 + df["日期"].dt.quarter

df_group = df.groupby("季別")

group_keys = list(df_group.groups.keys())
group_keys.sort()

train_parts = 4
ret_df = pd.DataFrame()
stock_df = pd.DataFrame()
for i in tqdm(range(len(group_keys) - train_parts)):
    train_keys = group_keys[i: i + train_parts]
    test_keys = group_keys[i + train_parts]

    train_df_list = []
    for k in train_keys:
        temp_df = df_group.get_group(k)
        train_df_list.append(temp_df)
    
    train_df = pd.concat(train_df_list)
    test_df = df_group.get_group(test_keys)
    test_df = test_df[test_df["日期"] == test_df["日期"].max()]
    
    # 建立XGBoost回歸模型
    model = XGBRegressor(
        n_estimators=100,
        max_depth=10,
        random_state=42,
        eval_metric='rmse'  # 設定評估指標
    )
    
    X_train = train_df.drop(["日期", "Close_T+N", "買入價格"], axis = 1)
    y_train = train_df[["Close_T+N"]]
    X_test = test_df.drop(["日期", "Close_T+N", "買入價格"], axis = 1)
    y_test = test_df[["Close_T+N"]]
    
    # 將資料帶入模型訓練
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    
    test_result_df = pd.DataFrame()
    test_result_df["股票代號"] = test_df['股票代號'].reset_index(drop = True)
    test_result_df["預測對數報酬"] = y_pred
    test_result_df["真實對數報酬"] = y_test.reset_index(drop = True)

    test_result_df = test_result_df.sort_values(["預測對數報酬"], ascending = [False])
    test_result_df = test_result_df.iloc[:10].reset_index(drop = True) # 預測前十檔

    ret_df.at[test_keys, "平均報酬率"] = np.exp(test_result_df["真實對數報酬"]).mean()
    
    stock_df[test_keys] = test_result_df["股票代號"]

ret_df["累計報酬率"] = ret_df["平均報酬率"].cumprod()
annual_ret = ret_df["累計報酬率"].iloc[-1]  ** (4 / ret_df.shape[0]) - 1
ret_df["平均報酬率"] -= 1
ret_df["累計報酬率"] -= 1
ret_df.to_excel("機器學習結果.xlsx")
stock_df.to_excel("機器學習選股.xlsx", index = False)

ret_df["累計最高報酬"] = ret_df["累計報酬率"].cummax()
ret_df["當下差距"] = ret_df["累計最高報酬"] - ret_df["累計報酬率"]
ret_df["MDD"] = ret_df["當下差距"].cummax()
#print(ret_df["MDD"].iloc[-1])
print(annual_ret)
ret_df.to_excel("回測結果.xlsx")