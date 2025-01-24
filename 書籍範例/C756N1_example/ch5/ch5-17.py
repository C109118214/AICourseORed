import random as rd
Num = rd.randint(0, 9)
count = 1
List_Num = [ ]
List_Num.append(Num)
while Num != 0:
    Num = rd.randint(0, 9)
    List_Num.append(Num)
    count += 1
print(List_Num)
print("%s%d%s" %("共產生亂數 ", count, " 次"))