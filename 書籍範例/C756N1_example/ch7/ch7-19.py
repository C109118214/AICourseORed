# ch7-19.py 功能: 依迴圈數呼叫繪圖長條圖自訂函數
import matplotlib.pyplot as plt
import numpy as np
def hist_plots(n, bins, cs):
# hist_plots( ): 依傳進來的資料, 組數與顏色繪製不同的長條圖
    data = np.random.randn(n)
    plt.hist(data, bins, color = cs)
    plt.show( )
num = [100, 500, 2000, 10000]
colorset = ['r', 'b', 'm', 'c']
group = 100
for i in range(len(num)):
    hist_plots(num[i], group, colorset[i])