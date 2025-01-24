# -*- coding: utf-8 -*-
# 匯入所需的庫
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier  # 載入KNN分類器
from get_cm import main as get_cm

result_list = []
for i in range(1, 5+1):
    data_path = "pima_fold/"
    X_train = pd.read_excel(f"{data_path}X_train_{i}.xlsx")
    y_train = pd.read_excel(f"{data_path}y_train_{i}.xlsx")
    X_valid = pd.read_excel(f"{data_path}X_valid_{i}.xlsx")
    y_valid = pd.read_excel(f"{data_path}y_valid_{i}.xlsx")
    
    # 建立KNN分類器模型
    model = KNeighborsClassifier(n_neighbors=5)  # 使用K最近鄰算法，n_neighbors設為5
    model.fit(X_train, y_train)
    
    # 預測測試集
    y_pred = model.predict(X_valid)
    
    # 計算出來的指標的Dict
    result = get_cm(y_valid, y_pred)
    result_list.append(result)

df = pd.DataFrame(result_list)
df = df.round(4)
print(df)
df.to_excel("KNN_結果.xlsx", index=False)


