# -*- coding: utf-8 -*-
list_1 = [[100, 4],
          [50, 1],
          [120, 2],
          [80, 3],
          [200, 2]
          ]

result_list = []
for i in list_1:
    result = i[0] / i[1]
    result_list.append(round(result,2))
print(result_list)