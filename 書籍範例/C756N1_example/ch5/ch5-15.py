Period = 10
print("%5s%8s%8s%8s%9s%9s%9s%9s%9s%9s%9s"  %("期數\利率", 
"1%", "2%", "3%", "4%", "5%","6%", "7%", "8%", "9%", "10%"))
for n in range(1, Period + 1):
    print("%7d" %(n), end = " ")
    for i in range(1, Period + 1):
        pvif = 1 / (1 + (i / 100)) ** n
        print("%8.4f"  %(pvif), end = " ")
    print( )