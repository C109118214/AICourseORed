f_name = input()
n = int(input())

# TODO
result_list = []
with open(f_name, "r") as f:
    data = f.read()
    data = data.replace("\n", " ")
    
    word_list = data.split(" ")
    word_set = set(word_list)
    
    for word in word_set:
        if word_list.count(word) == n:
            result_list.append(word)
    
    result_list.sort()
    for i in result_list:
        print(i)
