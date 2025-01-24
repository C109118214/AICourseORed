import random
Bingo = random.randint(1, 20)
while True:
    Num = int(input("請猜一個數字(1 到 20) = "))
    if Num == Bingo:
        print("恭喜, 猜中!!")
        break
    if Num > Bingo:
        print("請猜小一點!!")
    else:
        print("請猜大一點!!")