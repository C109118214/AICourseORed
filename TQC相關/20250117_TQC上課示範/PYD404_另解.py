# TODO
num = int(input())

result = ""
if num == 0:
    result = 0
else:
    while num > 0:
        digit = num % 10
        result+= str(digit) # 將個位數一一接到字串中
        num = num // 10 #刪除接過的個位數

print(result)
    
