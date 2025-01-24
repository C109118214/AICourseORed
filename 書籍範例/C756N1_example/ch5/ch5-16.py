sumi = 0    #預設累加的變數sumi為0
n = 5    #預設變數n為5
i = 1
while i < n + 1:
    sumi = sumi + i    #將sumi與i加總後累加給sumi
    print("第 %d 圈累加結果 ＝ %d"  %(i, sumi))
    i += 1