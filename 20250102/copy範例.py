# -*- coding: utf-8 -*-
list_1 = [1,2,3]
list_2 = list_1
print(id(list_1))
print(id(list_2))

# list_1新增4，list_2也會多出4
list_1.append(4)
print(list_2)

list_3 = [4,5,6]
list_4 = list_3.copy()
# copy之後，list_3、list_4沒有關係了，不會連動
print(id(list_3))
print(id(list_4))
list_3.append(7)

print(list_3)
print(list_4)
