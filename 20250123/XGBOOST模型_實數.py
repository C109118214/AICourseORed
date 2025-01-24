# -*- coding: utf-8 -*-
# 匯入所需的庫
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.preprocessing import StandardScaler

df = pd.read_excel("技術指標_實數.xlsx")
data_length = df.shape[0] # 確認資料的數量
split_point = int(data_length * 0.7) # 計算訓練集與測試集的分界點

X = df.drop(["日期", "Close_T+N", "買入價格"], axis = 1)
y = df[["Close_T+N"]]

# Z score標準化函式
#scaler = StandardScaler()
# 根據X的每一欄位的數據計算標準化的範圍
#scaler.fit(X)
# 將X進行轉換，變成標準化的數值
#X = scaler.transform(X)
# 從頭到分界點(訓練集)，從分界點到最後(測試集)
X_train = X[:split_point]
X_test = X[split_point:]
y_train = y[:split_point]
y_test = y[split_point:]


# 建立XGBoost回歸模型
model = XGBRegressor(
    n_estimators=100,
    max_depth=10,
    random_state=42,
    eval_metric='rmse'  # 設定評估指標
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

df_pred = test_data[test_data["model_pred"] > 0]

# 我一筆資金放進去
# 每一次的收益再次投入，所以前一次的交易結果會影響下一次的資金
# 計算累積報酬率
acc_ret = np.exp( df_pred["Close_T+N"] ).cumprod() -1 
acc_ret = acc_ret.iloc[-1]
print(acc_ret) 

final_amount = acc_ret + 1
total_cost = 1
# 年化報酬率
delta_days = test_data["日期"].iloc[-1] - test_data["日期"].iloc[0]
delta_days = delta_days.days# 取出差異幾天的數字
delta_years = delta_days / 365
# 年化報酬率
ann_ret = (final_amount / total_cost) ** (1 / delta_years) - 1
print(ann_ret)

# 評估模型
mse = mean_squared_error(df_pred["Close_T+N"], df_pred["model_pred"])
mae = mean_absolute_error(df_pred["Close_T+N"], df_pred["model_pred"])
r2 = r2_score(df_pred["Close_T+N"], df_pred["model_pred"])

print(f"Mean Squared Error (MSE): {mse}")
print(f"Mean Absolute Error (MAE): {mae}")
# 雖然R-Square不好，但如果實際值比預測值高很多，那也是有偏誤
print(f"R-squared (R²): {r2}")