f_name = input()
str_old = input()
str_new = input()
#TODO
with open(f_name, "r") as f:
    data = f.read() # 全部的文字一次讀取成字串
    
print("=== Before the replacement")
print(data)
#TODO

print("=== After the replacement")
data = data.replace(str_old, str_new)
print(data)
#TODO