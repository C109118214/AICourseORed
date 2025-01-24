# ch7-6.py功能 : 以自訂函數改寫選擇排序法並回傳陣列
import numpy as np
# 選擇排序法自訂函數
def selectionsort(ary):
    N = len(ary)
    for i in range(N - 1):
        min_index = i
        for j in range(i + 1 , N):
            if ary[min_index] > ary[j]:
                min_index = j
            # 將 ary[i] 與 ary[min_index] 互換值
        ary[i], ary[min_index] = ary[min_index], ary[i]
    return(ary)
# 主程式設定原始資料
ary = np.array([12, 31, 25, 45])
print("陣列排序前 = ", ary)
sls = selectionsort(ary)
print("選擇排序法後由小到大 = ", sls)