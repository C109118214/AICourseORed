# -*- coding: utf-8 -*-
Str_py = "Python is Good for Beginners"
print(Str_py.replace("Good", "Best"))

print(Str_py.replace("n", ""))

date = "2024/12/31"
print(date.replace("/", "-"))

print(Str_py.find("is"))
print(Str_py.find("are"))
print(Str_py.find("n")) # 只會顯示第一個找到的位置
print(Str_py.find("n", 6)) # 從index為6後找尋

print(Str_py.count("is"))

split_result = Str_py.split(" ")
print(split_result)
print(split_result[1:4])

date_2 = date.split("/")
print(date_2)
join_sign = " "
print(join_sign.join(date_2))

print(Str_py.startswith("Python"))
print(Str_py.endswith("Beginners"))

