import random
a = b = c = d = e = f = 0
while True:
    a = random.randint(1, 42)
    b = random.randint(1, 42)
    c = random.randint(1, 42)
    d = random.randint(1, 42)
    e = random.randint(1, 42)
    f = random.randint(1, 42)
    if (a != b and a != c and a != d and a != e and a != f):
        if (b != c and b !=d and b != e and b != f):
            if (c != d and c != e and c != f):
                if (d != e and d != f):
                    if (e != f):
                        break
print("六個號碼為:", a, b, c, d, e, f)