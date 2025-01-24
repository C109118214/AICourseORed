# TODO
def compute(sentence, char):
    times = 0 # 紀錄出現幾次
    char_len = len(char) # 尋找的目標長度
    # 從第0個字元開此走訪
    for i in range( len(sentence) ):
        # 照順序取出字段
        # 如果字段與要尋找的目標相同則次數+1
        if char == sentence[i : i + char_len]:
            times +=1
    return times

sentence = input()
char = input()
result = compute(sentence, char)
print(f"{char} occurs {result} time(s)")
"""
_ occurs _ time(s)
"""
