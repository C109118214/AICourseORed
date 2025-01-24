# TODO
num = int(input())# 要判斷幾句
for i in range(num):
    # 輸入的句子
    sentence = input()
    #全部轉小寫
    sentence = sentence.lower()
    #去除空格
    sentence = sentence.replace(" ", "")
    # 轉換成集合去重複
    letter_set = set(sentence)
    # 這個集合長度是否是26
    print(len(letter_set) == 26)
