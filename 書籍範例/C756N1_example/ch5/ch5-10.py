import math
List_2330 = [278.5, 279.5, 283, 285, 283, 275.5, 271.5, 274, 267.5, 273]
n = len(List_2330)
MeanV = sum(List_2330) / n
print("股價平均數 = ", MeanV)
sumi = 0
for i in range(len(List_2330)):
    sumi += (List_2330[i] - MeanV) ** 2
S = math.sqrt(sumi / (n - 1))
print("股價標準差 = ", round(S, 4))