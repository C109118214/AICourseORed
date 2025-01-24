# -*- coding: utf-8 -*-
def local_func():
   var = "我是區域變數(local varible)"
   print("自訂函數內", var)
local_func()
var = "我是全域變數(global varible)"
print("全域中", var) # 全域範圍中，無法呼叫區域變數