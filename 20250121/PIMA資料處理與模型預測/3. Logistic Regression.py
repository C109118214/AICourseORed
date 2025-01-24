# 匯入所需的庫
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from get_cm import main as get_cm

result_list = []
for i in range(1, 5+1):
    data_path = "pima_fold/"
    X_train = pd.read_excel(f"{data_path}X_train_{i}.xlsx")
    y_train = pd.read_excel(f"{data_path}y_train_{i}.xlsx")
    X_valid = pd.read_excel(f"{data_path}X_valid_{i}.xlsx")
    y_valid = pd.read_excel(f"{data_path}y_valid_{i}.xlsx")
    
    # 建立邏輯斯回歸模型
    model = LogisticRegression()
    model.fit(X_train, y_train)
    
    # 預測測試集
    y_pred = model.predict(X_valid)
    
    # 計算出來的指標的Dict
    result = get_cm(y_valid, y_pred)
    result_list.append(result)

df = pd.DataFrame(result_list)
df = df.round(4)
print(df)
df.to_excel("驗證集結果/LR.xlsx", index = False)
    # =============================================================================
# # 顯示混淆矩陣
# cm = confusion_matrix(y_test, y_pred)
# print("Confusion Matrix:")
# print(cm)
# 
# # 顯示分類報告
# report = classification_report(y_test, y_pred)
# print("Classification Report:")
# print(report)
# 
# # 畫出混淆矩陣圖
# plt.figure(figsize=(6, 4))
# sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['No Diabetes', 'Diabetes'], yticklabels=['No Diabetes', 'Diabetes'])
# plt.ylabel('Actual')
# plt.xlabel('Predicted')
# plt.title('Confusion Matrix')
# plt.show()
# =============================================================================
