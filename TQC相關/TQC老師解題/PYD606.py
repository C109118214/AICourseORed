def compute(lst):
    for row in lst:
        for val in row:
            print(f"{val:4}", end="")
        print()

# 輸入rows和cols
rows = int(input())
cols = int(input())

# 建立二維串列
lst = []
for row in range(rows):
    lst_row = []
    for col in range(cols):
        lst_row.append(col - row)
    lst.append(lst_row)

# 呼叫函式並輸出結果
compute(lst)