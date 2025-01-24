# -*- coding: utf-8 -*-

class_list = ["A", "B", "C"] # 班級列表
class_num = len(class_list) # 班級的數量
game_set_list = [] # 儲存組合的串列
# 班級之間兩兩配對
# i為0，j會跑過1,2
# i為1，j會跑過2
# i為2，j不會跑
for i in range(class_num): # 從第一個班級，列舉其他班級的配對
    # 配對的目標
    for j in range(i + 1, class_num):
        # 將每個班級的名稱，根據i,j取出，放入list中代表配對
        game_set = [ class_list[i], class_list[j] ]
        # 將配對放入game_set_list(儲存組合的串列)
        game_set_list.append(game_set)
print(game_set_list)

# 將每個組合輸出
for g_set in game_set_list:
    print(g_set[0], "班對上", g_set[1], "班")
        