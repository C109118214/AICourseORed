# ch7-22.py 功能: 以自訂函數撰寫氣泡排序法
import numpy as np
def bub_search(ary):
# bub_search( ): 傳入的資料進行排序
    N = len(ary)
    for i in range(N - 1):
        for j in range(N - i - 1):
            if ary[j] < ary[j + 1]:
                # 將ary[j]與ary[j + 1]互換值
                ary[j], ary[j + 1] = ary[j + 1], ary[j]
    return(ary)
arr = np.fromstring(input('請輸入以空白隔開的資料如 6 4 8 5 = '), dtype = int, sep = ' ')
print('原始未排序陣列資料 = ', arr)
arr = bub_search(arr)
print('已排序陣列資料 = ', str(arr))