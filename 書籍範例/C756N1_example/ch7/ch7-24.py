# ch7-24.py 功能: 以自訂函數撰寫直線法折舊費用
import numpy as np
def straightline(cost, salvage, n):
# straightline: 直線法公式
    return((cost - salvage) / n)
def slinetable(ary, expense, cost, row, col):
# slinetable: 計算折舊費用分攤表
    acm_exp = 0
    for i in range(0, row):
        ary[i][0] = i
        ary[i][1] = expense
        ary[i][2] = expense + acm_exp
        ary[i][3] = cost - ary[i][2]
        acm_exp = ary[i][2]
    return(ary)
cost = int(input('請輸入資產成本= '))
salvage = int(input('請輸入資產殘值 = '))
row = int(input('請輸入資產使用年限 = '))
col = 4  # 折舊費用分攤表共有 4 個欄位
ary = np.zeros((row, col))
sline_exp = straightline(cost, salvage, row)
slt = slinetable(ary, sline_exp, cost, row, col)
print('%3s%8s%8s%8s' % ('年度', '折舊費用', '累計折舊', '期末帳面價值'))
for i in range(0, row):
    print('%4d%10d%12d%14d' % (slt[i][0] + 1, slt[i][1], slt[i][2], slt[i][3]))