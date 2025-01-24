# -*- coding: utf-8 -*-
def local_func():
    print("自訂函數中可以用全域的變數", global_var)
    
global_var = "我是全域變數(global varible)"
local_func()