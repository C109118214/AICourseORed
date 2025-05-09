# -*- coding: utf-8 -*-
# 匯入所需的庫
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from get_cm import main as get_cm
data_path = "pima_fold/"

# 讀取測試集資料
X_test = pd.read_excel(f"{data_path}X_test.xlsx")
y_test = pd.read_excel(f"{data_path}y_test.xlsx")
# 放五個不同交叉分析資料訓練的模型，對於測試集的預測結果
test_result_df = pd.DataFrame() 

result_list = []
for i in range(1, 5+1):
    
    X_train = pd.read_excel(f"{data_path}X_train_{i}.xlsx")
    y_train = pd.read_excel(f"{data_path}y_train_{i}.xlsx")
    X_valid = pd.read_excel(f"{data_path}X_valid_{i}.xlsx")
    y_valid = pd.read_excel(f"{data_path}y_valid_{i}.xlsx")
    
    # 建立XGBoost模型
    model = XGBClassifier(n_estimators=100,
                          max_depth=10,
                          random_state=42,
                          use_label_encoder=False,  # 避免XGBoost的警告
                          eval_metric='logloss'  # 設定評估指標
                          )
    model.fit(X_train, y_train)
    
    # 預測測試集
    y_pred = model.predict(X_valid)
    
    # 計算出來的指標的Dict
    result = get_cm(y_valid, y_pred)
    result_list.append(result)
    
    # 將Test資料放入模型預測，將預測結果整理到一個DF
    y_test_pred = model.predict(X_test)
    test_result_df[i] = y_test_pred

print(test_result_df)
df = pd.DataFrame(result_list)
df = df.round(4)

# 找出驗證集Accuracy最高的index，作為測試集的結果
max_acc_index = df["Accuracy"].idxmax()

# 根據找出來的index，挑選測試集使用的預測結果
# 實務上只能做到這裡，因為實務上沒有y_test可以比較
test_result = test_result_df[max_acc_index+1]
# 以y_test對答，看看最後的成果
test_result = get_cm(y_test, test_result)
print(test_result)

print(df)
df.to_excel("驗證集結果/XGBoost.xlsx", index=False)
