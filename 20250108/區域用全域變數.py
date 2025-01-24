# -*- coding: utf-8 -*-
def dec_glo():
    # 宣告num_var是使用全域變數
    global num_var
    num_var = num_var + 10
    print(f"在dec_glo函數內{num_var},id為{id(num_var)}")
   
num_var = 5
print(f"呼叫dec_glo前{num_var},id為{id(num_var)}")
dec_glo()
print(f"呼叫dec_glo後{num_var},id為{id(num_var)}")