# -*- coding: utf-8 -*-

s1 = [[90, 82, 85],
      [70, 75, 71],
      [60, 55, 80]]

s2 = [[85, 80, 80],
      [80, 70, 75],
      [70, 60, 71]]

mean_diff_list = []
for i in range(3): # 走訪每一科的分數
    diff = 0 # 總差距
    for k in range(3):
        # 以同一個位置的index取出兩個學期的分數進行相減
        diff+= s2[i][k] - s1[i][k]
        print(i, k, s1[i][k], s2[i][k])
    mean_diff = diff / 3 # 將進步幅度平均
    mean_diff_list.append(mean_diff) # 將單科的進步幅度放入串列
print(mean_diff_list)
        