import random
Num = int(input("請問您要骰幾次:"))
Dice = [0] * 6   #產生一個6個元素的串列
#統計骰子6個點各自出現的次數與機率
for i in range(Num):
    index = random.randint(1, 6)
    #依index的數字對應用串列的索引位置-1，累加1
    Dice[index - 1] += 1  
#印出6個點出現的次數與機率
for i in range(len(Dice)):
    print("%d點, 出現次數 = %d, 出現機率為%.2f"  %(i + 1, Dice[i], Dice[i] / Num))