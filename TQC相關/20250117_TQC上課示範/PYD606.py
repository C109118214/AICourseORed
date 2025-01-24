# TODO

def compute(row, col):
    # 產生從0開始到col - 1的數列
    num_list = list(range(col))
    
    # 需要幾列，就走訪幾次
    for r in range(row):
        # 下一列式上一列的-1，用r去調整
        for num in num_list:
            num = num - r
            # 輸出補空格到第4位數的整數
            # 不換行
            print(f"{num:4d}", end = "")
        print() # 一列結束之後，換行
 
row = int(input()) # 幾列
col = int(input()) # 一列數字有幾個
compute(row, col)