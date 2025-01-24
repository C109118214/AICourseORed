# -*- coding: utf-8 -*-
# W代表寫入
# 絕對路徑

#f = open("C:/Users/user/Desktop/新尖兵授課相關/20250109/output/test2.txt", "w")
#f = open("C:\\Users\\user\\Desktop\\新尖兵授課相關\\20250109\\output\\test3.txt","w")
# 相對路徑
f = open("output/test.txt", "w")
f.write("第一行\n")
f.write("第二行")
f.close() # 關閉檔案