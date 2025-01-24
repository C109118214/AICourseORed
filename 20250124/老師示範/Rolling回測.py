# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from tqdm import tqdm
from xgboost import XGBRegressor
from sklearn.preprocessing import StandardScaler
# 讀取資料
df = pd.read_csv("所有股票技術指標.csv")
df = df[df["日期"] >= "2010-01-01"] # 篩選2010以後的資料

# =============================================================================
# scaler = StandardScaler()
# Z_score_columns = ['成交股數', '成交金額', '開盤價', '最高價', '最低價', '收盤價', '成交筆數', 'MA5', 'MA10',
#        'MA20', 'EMA_20', 'RSI_14', 'MACD', 'MACD_Signal', 'MACD_Hist',
#        'BB_Upper', 'BB_Middle', 'BB_Lower', 'ADX_14', 'ATR_14', 'CCI_20',
#        'SlowK', 'SlowD', 'SAR']
# 
# scaler.fit(df[Z_score_columns])
# df[Z_score_columns] = scaler.transform(df[Z_score_columns])
# =============================================================================
# 確保日期欄位為datetime格式
df["日期"] = pd.to_datetime(df["日期"])
# 從日期抓處年、季，並且合併在一起，如201001，代表2010年第一季
df["季別"] = df["日期"].dt.year * 100 + df["日期"].dt.quarter

df_group = df.groupby("季別") #　根據季別分組
# 將季別列出，轉換成list，並從小到大排序
group_keys = list(df_group.groups.keys())
group_keys.sort()

train_parts = 4 # 一季測試集，對應4季訓練集
ret_df = pd.DataFrame() # 放每個測試集的報酬
stock_df = pd.DataFrame() # 放每個測試集選到的股票
# 走訪用迴圈group_keys
for i in range(len(group_keys) - train_parts):
    # 取出i到i+3季，如201001到201004的資料
    train_keys = group_keys[i: i + train_parts]
    # 取出i+4季，如201101的資料
    test_keys = group_keys[i + train_parts]
    
    # 將訓練集資料從group取出、合併成一個DataFrame
    train_df_list = []
    for k in train_keys:
        temp_df = df_group.get_group(k)
        train_df_list.append(temp_df)
    train_df = pd.concat(train_df_list)
    
    # 取出測試集，並篩選出這季最後一天的資料，當成預測目標
    # 用來交易
    test_df = df_group.get_group(test_keys)
    test_df = test_df[test_df["日期"] == test_df["日期"].max()]

    # 建立XGBoost回歸模型
    model = XGBRegressor(
        n_estimators=100,
        max_depth=10,
        random_state=42,
        eval_metric='rmse'  # 設定評估指標
    )
    
    # 分離X、Y
    X_train = train_df.drop(["日期", "Close_T+N", "買入價格", "股票代號", "季別"], axis = 1)
    y_train = train_df[["Close_T+N"]]
    X_test = test_df.drop(["日期", "Close_T+N", "買入價格", "股票代號", "季別"], axis = 1)
    y_test = test_df[["Close_T+N"]]
    
    # 將訓練集資料帶入模型訓練
    model.fit(X_train, y_train)
    # 將訓練好的模型用來預測測試集資料
    y_pred = model.predict(X_test)
    
    # 新增一個DF，放股票代號、預測對數報酬、真實對數報酬
    test_result_df = pd.DataFrame()
    # 因為篩選後的test_df的index不是從0開始編號
    # 所以要重置成從0開始編號，以便預測對數報酬、真實對數報酬
    # 可以對應上
    test_result_df["股票代號"] = test_df['股票代號'].reset_index(drop = True)
    test_result_df["預測對數報酬"] = y_pred
    test_result_df["真實對數報酬"] = y_test.reset_index(drop = True)
    
    # 根據預測對數報酬由大到小排序，找出前10筆資料當成投資組合
    test_result_df = test_result_df.sort_values(["預測對數報酬"], ascending = [False])
    test_result_df = test_result_df.iloc[:10].reset_index(drop = True) # 預測前十檔
    
    # 還原對數報酬，計算投資組合的平均報酬，假設為資金分配為等權重
    # 記錄到ret_df，等全部做完再一起評估
    ret_df.at[test_keys, "平均報酬率"] = np.exp(test_result_df["真實對數報酬"]).mean()
    # 記錄這一季選到的股票代號
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