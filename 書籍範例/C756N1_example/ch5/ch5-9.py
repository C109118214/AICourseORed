Rev = [60000, 75000, 50000]
Exp = [50000, 70000, 56000]
print("%5s%5s%8s%10s%10s" 
       %(" 年度", "收益", "費損", "淨利(淨損)", "佔收益%"))
for i in range (len(Rev)):
    Net = Rev[i] - Exp[i]
    Persent = (Net / Rev[i]) * 100
    print("%5d%10d%10d%12d%13.3f" 
           %(i+1, Rev[i], Exp[i], Net, Persent))