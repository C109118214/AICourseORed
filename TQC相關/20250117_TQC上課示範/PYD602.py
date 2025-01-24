# TODO
total = 0
for i in range(5):
    card = input()
    if card == "A": 
        total += 1
    elif card == "J":
        total += 11
    elif card == "Q":
        total += 12
    elif card == "K":
        total += 13
    else:
        total += int(card)
        
print(total)