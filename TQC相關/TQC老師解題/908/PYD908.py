f_name = input()
n = int(input())

# TODO
word_list = []
with open(f_name, "r") as f:
    data = f.read()
    data = data.replace("\n", " ")
    data = data.split(" ")
    
    data_set = set(data)
    
    for word in data_set:
        if data.count(word) == n:
            word_list.append(word)
    
    word_list.sort()
    for word in word_list:
        print(word)

