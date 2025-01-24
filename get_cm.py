# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 13:57:47 2025

@author: USER
"""

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
def main(y_valid, y_pred):
    # 顯示準確度
    accuracy = accuracy_score(y_valid, y_pred)
    #print(f"Accuracy: {accuracy:.4f}")
    
    cm = confusion_matrix(y_valid, y_pred,
                          labels = [1, 0])
    #print(cm)
    
    tp, fp, fn, tn = cm.ravel()
    tpr = tp / (tp + fn) # 真陽性率，有多少真實的陽性被預測出來
    tnr = tn / (fp + tn) # 真陰性率，有多少真實的陰性被預測出來
    ppv = tp / (tp + fp) # 預測出來的結果有多少真的是陽性
    npv = tn / (tn + fn) # 預測出來的結果有多少真的是陰性
# =============================================================================
#     print("真陽性率", tpr)
#     print("真陰性率", tnr)
#     print("陽性預測值", ppv)
#     print("陰性預測值", npv)
# =============================================================================
    result = {
        "Accuracy" : accuracy,
        "TP" : tp,
        "FP" : fp,
        "FN" : fn,
        "TN" : tn,
        "TPR" : tpr,
        "TNR" : tnr,
        "PPV" : ppv,
        "NPV" : npv
        }
    
    
    return result 