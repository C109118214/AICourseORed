# TODO
SSN = input()
# 檢查index 3、6的地方是否為-
check_1 = SSN[3] == "-" and SSN[6] == "-"
SSN = SSN.replace("-", "") # 去除-
check_2 = SSN.isdigit() # 是否全都由數字組成

# 兩個檢查條件都成立，就通過
if check_1 and check_2:
    print("Valid SSN")
else:
    print("Invalid SSN")

"""
Valid SSN
Invalid SSN
"""