# TODO
number_num = int(input())
for i in range(number_num):
    num = int(input())
    
    temp = num
    total = 0
    while temp > 0:
        a, b = divmod(temp, 10)
        total+= b
        temp = a

    print(f"Sum of all digits of {num} is {total}")
   
"""
Sum of all digits of _ is _
"""