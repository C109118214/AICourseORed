# -*- coding: utf-8 -*-
# 定義聖誕樹
# 輸入聖誕樹層數
tree_layers = int( input("請輸入聖誕樹層數：") )

def tree_single_layer(current_layer, max_layer):
    # 第一層特別處理
    if current_layer == 1:
        for i in range(4):
            print(" " * (3-i+max_layer-current_layer) + "* " * i) # 用最大層數與現在的層數調整輸出結果
    # 其他層
    else:
        max_length = current_layer + 3 # 每層三層
        for i in range(current_layer, max_length):
            print(" " * (max_length -1 -i+max_layer- current_layer) + "* " * i)  # 用最大層數與現在的層數調整輸出結果
# 固定給三層的樹幹，並根據樹的層數調整位子
def tree_root(max_layer):
    for i in range(3):
        print(" " * max_layer +"*" * 3) # 樹幹粗固定3個*
        
# 用迴圈將每一層透過自訂函數輸出
for layer in range(1, tree_layers+1):
    tree_single_layer(layer, tree_layers)

tree_root(tree_layers) # 輸出樹幹

print("------------")