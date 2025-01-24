# -*- coding: utf-8 -*-

Dict_C1 = {
    "Name" : "Steven",
    "Age" : 25,
    "Investment" : 1000.25
    }
print(Dict_C1)

print(Dict_C1["Age"])

#print(Dict_C1["EMAIL"])

#print(Dict_C1.get("EMAIL"))
# 在字典中加入新的key : value
Dict_C1["EMAIL"] = "12345@gmail.com"
print(Dict_C1)
print(Dict_C1["EMAIL"])
print("----------")
Dict_C1["EMAIL"] = "AAAAAA@gmail.com"
print(Dict_C1)
print(Dict_C1["EMAIL"])
print("----------")
print(Dict_C1.keys())
for k in Dict_C1.keys():
    print(Dict_C1[k])