List_2330 = [278.5, 279.5, 283, 285, 283, 275.5, 271.5, 274, 267.5, 273]
ROI = [ ]
for i in range(len(List_2330) - 1):
    t = List_2330[i + 1]
    t_1 = List_2330[i]
    ROI.append(round(((t - t_1) / t_1) * 100, 4))
print("日報酬率 = ", ROI)
print("最大值 = ", max(ROI)) 
print("最小值 = ", min(ROI)) 
print("平均數 = ", round(sum(ROI) / len(ROI), 4)) 