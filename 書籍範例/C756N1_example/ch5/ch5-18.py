Elastic = float(input("請輸入球彈力係數(0 ~ 0.99) = "))
Height = int(input("請輸入球回彈的高度 = "))
count = 0
while Height > 0.01:    #假設小於0.01公尺為靜止
    Height = Height * Elastic
    count += 1
    print("第 %d 圈，高度 = %6.4f"  %(count, Height))
print("共彈了%d次"  %(count))