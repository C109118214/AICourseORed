# TODO
SSN = input()
check_1 = (SSN[3] == "-") and (SSN[6] == "-")
num = SSN.replace("-", "")
check_2 = num.isdigit()
if check_1 and check_2:
    print("Valid SSN")
else:
    print("Invalid SSN")



"""
Valid SSN
Invalid SSN
"""