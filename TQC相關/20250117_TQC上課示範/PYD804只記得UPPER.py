# TODO
sentence = input()
print(sentence.upper()) # 全部大寫
# 用空格切割字串變成list
sen_list = sentence.split(" ")

result = ""
for word in sen_list:
    # 單字第一個字母大寫，其他小寫
    word = word[0].upper() + word[1:].lower()
    result += word + " "
result = result[:-1] # 去掉最後一個空格
print(result)