# -*- coding: utf-8 -*-
# 匯入所需的庫
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from get_cm import main as get_cm
from sklearn.preprocessing import StandardScaler

df = pd.read_excel("技術指標.xlsx")
data_length = df.shape[0] # 確認資料的數量
split_point = int(data_length * 0.7) # 計算訓練集與測試集的分界點

X = df.drop(["日期", "Close_T+N", "買入價格", "Profit"], axis = 1)
y = df[["Close_T+N"]]

# Z score標準化函式
scaler = StandardScaler()
# 根據X的每一欄位的數據計算標準化的範圍
scaler.fit(X)
# 將X進行轉換，變成標準化的數值
X = scaler.transform(X)
# 從頭到分界點(訓練集)，從分界點到最後(測試集)
X_train = X[:split_point]
X_test = X[split_point:]
y_train = y[:split_point]
y_test = y[split_point:]

# 建立XGBoost模型
model = XGBClassifier(n_estimators=100,
                          max_depth=10,
                          random_state=42,
                          use_label_encoder=False,  # 避免XGBoost的警告
                          eval_metric='logloss'  # 設定評估指標
                          )
# 將資料帶入模型訓練
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
# 將模型訓練的結果放回原始資料，篩選，查看profit
# 測試集的原始資料
# 包含"日期", "Close_T+5", "買入價格", "Profit"欄位
# 要用Profit來看總共賺了多少錢
test_data = df.iloc[split_point:]
# 將預測的結果放回原始資料 
test_data["model_pred"] = y_pred
# 篩選預測為1的進行買入持有五天
df_pred = test_data[test_data["model_pred"] == 1]

# 交易假設
# 每一次都投入相同的金額，前後一次交易相互獨立
# 每一次交易買1股，所有交易獲利的加總
# 所以總成本為買入價格的加總
# 最終金額就是總成本 + 總獲利
total_profit = df_pred["Profit"].sum()
total_cost =  df_pred["買入價格"].sum() #總成本
final_amount = total_cost + total_profit # 最終金額
print(total_profit) #將有購買的股票獲利進行加總
print(get_cm(y_test, y_pred))

delta_days = test_data["日期"].iloc[-1] - test_data["日期"].iloc[0]
delta_days = delta_days.days# 取出差異幾天的數字
delta_years = delta_days / 365
# 年化報酬率
ann_ret = (final_amount / total_cost) ** (1 / delta_years) - 1
print(ann_ret)
