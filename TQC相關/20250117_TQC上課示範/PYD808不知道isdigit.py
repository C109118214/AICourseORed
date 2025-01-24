# TODO
SSN = input()
# 檢查index 3、6的地方是否為-
check_1 = SSN[3] == "-" and SSN[6] == "-"
SSN = SSN.replace("-", "") # 去除-
try:
    int(SSN) # 試著將SSN轉換成整數
    check_2 = True # 沒出錯代表他都是數字組成
except:
    check_2 = False # 出錯代表有不是數字的值
    
# 兩個檢查條件都成立，就通過
if check_1 and check_2:
    print("Valid SSN")
else:
    print("Invalid SSN")

    
"""
Valid SSN
Invalid SSN
"""