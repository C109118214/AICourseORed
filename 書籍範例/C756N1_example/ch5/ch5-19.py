Num_A = int(input("請輸入A整數 = "))
Num_B = int(input("請輸入B整數 = "))
Temp_A = Num_A
Temp_B = Num_B
while (Num_B != 0):    # 判斷當Num_B不等於0時進迴圈
    # Num_A除以Num_B取餘數給Num_B; 把Num_B指派給Num_A
    Num_A, Num_B = Num_B, Num_A % Num_B
gcd = Num_A
print("%d和%d的最大公因數gcd為 : %d"  %(Temp_A, Temp_B, gcd))
#藉由gcd找到lcm
print("%d和%d的最小公倍數lcm為 : %d" 
      %(Temp_A, Temp_B, ((Temp_A * Temp_B) / gcd)))