# TODO
while True: #預設是無窮迴圈，一直執行
    height = int(input())
    # 身高是-9999，結束迴圈
    if height == -9999:
        break
    
    weight = int(input())

    BMI = weight / (height / 100) ** 2
    if BMI < 18.5:
        result = "under weight"
    elif BMI < 25:
        result = "normal"
    elif BMI < 30:
        result = "over weight"
    else:
        result = "fat"
    print(f"BMI: {BMI:.2f}")
    print(f"State: {result}")


"""
fat
over weight
normal
under weight
BMI: _
State: _
"""