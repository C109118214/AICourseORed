# -*- coding: utf-8 -*-
import pandas as pd
from sklearn.model_selection import train_test_split, KFold
from sklearn.preprocessing import StandardScaler
import joblib
save_path = "pima_fold/"
df = pd.read_excel("fillna_pima.xlsx")

# 將y從資料中去除，否則訓練的模型只會抄答案
X = df.drop(["是否有糖尿病"], axis = 1)
# 為了後續方便用DataFrame方法處理
# 所以即便只選出一個欄位也用list帶入
# y就是DataFrame格式
y = df[["是否有糖尿病"]]

# 因為要存檔，要換回pandas，保留欄位名稱，不一定要做這一步
X_columns = X.columns 
y_columns = "是否有糖尿病"

# Z score標準化函式
scaler = StandardScaler()
# 根據X的每一欄位的數據計算標準化的範圍
scaler.fit(X)
# 將X進行轉換，變成標準化的數值
X = scaler.transform(X)
# Y本身就是0、1，所以不用轉換

# 儲存正規化的標準
joblib.dump(scaler, f'{save_path}std_scaler.bin')

# 將資料集切割成 9:1 的訓練及與測試集，切分好的數據是Numpy
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size = 0.1,
    random_state = 43
    )

# Numpy不能直接存成EXCEL，所以要轉換回Pandas
# 將切分好的數據轉換回Pandas，以便存檔
X_train = pd.DataFrame.from_records(X_train, columns = X_columns)
y_train = pd.DataFrame.from_records(y_train)

# 測試集下面不會處理，所以直接存檔
X_test = pd.DataFrame.from_records(X_test, columns = X_columns)
y_test = pd.DataFrame.from_records(y_test)
X_test.to_excel(f"{save_path}X_test.xlsx", index = False)
y_test.to_excel(f"{save_path}y_test.xlsx", index = False)

# 設定為5倍交叉驗證，挑選順序設定為隨機
kf = KFold(n_splits = 5, shuffle=True)

# 根據交叉分析切出來的資料，分別存檔
count = 1
for train_index, valid_index in kf.split(X_train):
    X_fold_train = X_train.iloc[train_index]
    y_fold_train = y_train.iloc[train_index]
    X_fold_valid = X_train.iloc[valid_index]
    y_fold_valid = y_train.iloc[valid_index]
    
    X_fold_train.to_excel(f"{save_path}X_train_{count}.xlsx", index = False)
    y_fold_train.to_excel(f"{save_path}y_train_{count}.xlsx", index = False)
    X_fold_valid.to_excel(f"{save_path}X_valid_{count}.xlsx", index = False)
    y_fold_valid.to_excel(f"{save_path}y_valid_{count}.xlsx", index = False)
    count+= 1
