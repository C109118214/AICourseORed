# -*- coding: utf-8 -*-

def discount(total):
    if total >= 999:
        total*= 0.85
    elif total >= 499:
        total*= 0.95
    
    return total

num = int(input("請輸入購物金額："))
result = discount(num)

print(f"折扣後的金額為：{result}")