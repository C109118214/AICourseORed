# ch7-13.py功能 : 印出變數所屬區域變數範圍或全域變數範圍
def call_globalvar( ):
# call_GlobalVar : 在函數內印出全域變數
    print(global_var, '在自訂函數呼叫並印出全域變數')
global_var = 'I am a global variable'
call_globalvar( )
print(global_var, '在主程式印出全域變數')