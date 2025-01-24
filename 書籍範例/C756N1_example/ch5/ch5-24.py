Find = True    # 進迴圈的條件設為True
while Find:
    Num = int(input("鈔票共有多少張 = "))
    Red = int(input("共有多少錢 = "))
    flag = False
    for Five in range(0, Num + 1):   # Five代表500元的張數
        One = Num - Five    #2
	  佰元張數是由總張數減去伍佰元張數
        if (Red == (One * 100 + Five * 500)):
            flag = True
            break
    if (flag == False):
        print("你輸入的資料無法找到解!!")
        print("輸入範例 : 鈔票共有多少張 = 5，共有多少錢 = 900")
        print("結果 : 500有 1 張, 100元有 4 張, 共 900 元")
    else:
        print("500有 %d 張, 100元有 %d 張, 共 %d 元"  %(Five, One, Red))
        Find = False