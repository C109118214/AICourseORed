# TODO
sen_num = int(input())
for n in range(sen_num):
    sentence = input()
    letter_set = set()
    sentence = sentence.lower()
    for i in sentence:
        if i == " ":
            continue
        letter_set.add(i)
    
    print(len(letter_set) == 26)