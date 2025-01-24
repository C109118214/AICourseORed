count = 0    #累加1到100能被7與5整除的個數
factor = [ ]    #記錄1到100能被7與5整除的因數
sumi = 0    #累加1到100能被7與5整除的因數總和
for i in range(1, 101):
    if (i % 7 == 0) and (i % 5 == 0):
        count = count + 1
        sumi = sumi + i
        factor.append(i)
print("1 到 100 能被7與5 整除的因數 =", factor)
print("1 到 100 能被7與5 整除的個數 =", count)
print("1 到 100 能被7與5 整除的因數總和為 =", sumi)