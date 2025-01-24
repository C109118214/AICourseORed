# -*- coding: utf-8 -*-
from sklearn.model_selection import  KFold
list_1 = list(range(1, 11))

# 設定為5倍交叉驗證，挑選順序設定為隨機
kf = KFold(n_splits = 5, shuffle=True) 

for train_index, valid_index in kf.split(list_1):
    print(train_index, valid_index)