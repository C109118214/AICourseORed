# -*- coding: utf-8 -*-
# 匯入所需的庫
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC  # 載入SVM
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from get_cm import main as get_cm

result_list = []
for i in range(1, 5+1):
    data_path = "pima_fold/"
    X_train = pd.read_excel(f"{data_path}X_train_{i}.xlsx")
    y_train = pd.read_excel(f"{data_path}y_train_{i}.xlsx")
    X_valid = pd.read_excel(f"{data_path}X_valid_{i}.xlsx")
    y_valid = pd.read_excel(f"{data_path}y_valid_{i}.xlsx")
    
    # 建立SVM模型
    model = SVC(kernel='linear', random_state=42)  # 使用線性核
    model.fit(X_train, y_train)
    
    # 預測測試集
    y_pred = model.predict(X_valid)
    
    # 計算出來的指標的Dict
    result = get_cm(y_valid, y_pred)
    result_list.append(result)

df = pd.DataFrame(result_list)
df = df.round(4)
print(df)
df.to_excel("SVM_結果.xlsx", index=False)
