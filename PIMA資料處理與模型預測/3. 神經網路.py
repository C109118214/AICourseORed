# -*- coding: utf-8 -*-
# 匯入所需的庫
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from get_cm import main as get_cm

result_list = []
for i in range(1, 5+1):
    data_path = "pima_fold/"
    X_train = pd.read_excel(f"{data_path}X_train_{i}.xlsx")
    y_train = pd.read_excel(f"{data_path}y_train_{i}.xlsx")
    X_valid = pd.read_excel(f"{data_path}X_valid_{i}.xlsx")
    y_valid = pd.read_excel(f"{data_path}y_valid_{i}.xlsx")
    
    # 建立Keras神經網絡模型
    model = Sequential()
    model.add(Dense(100, input_dim=X_train.shape[1], activation='relu'))  # 第一層隱藏層，100個神經元，使用ReLU激活函數
    model.add(Dense(64, activation='relu'))  # 第二層隱藏層，64個神經元，使用ReLU激活函數
    model.add(Dense(32, activation='relu'))  # 第三層隱藏層，32個神經元，使用ReLU激活函數
    model.add(Dense(1, activation='sigmoid'))  # 輸出層，使用Sigmoid激活函數，二分類問題
    
    # 編譯模型
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    
    # 訓練模型
    model.fit(X_train, y_train, epochs=100, batch_size=32, verbose=0)
    
    # 預測測試集
    y_pred = (model.predict(X_valid) > 0.5).astype("int32")  # 轉換為0或1
    
    # 計算出來的指標的Dict
    result = get_cm(y_valid, y_pred)
    result_list.append(result)

df = pd.DataFrame(result_list)
df = df.round(4)
print(df)
df.to_excel("驗證集結果/NN.xlsx", index=False)
