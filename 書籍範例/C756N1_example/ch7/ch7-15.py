# ch7-15.py功能: 印出函數內含函數的封閉變數
def out_func( ):
# out_func: 印出區域變數並呼叫子函數 in_func
    var = 'local variable'
    print('在out_func自訂函數內的區域變數 var = ', var)
    def in_func( ):
    # in_func: 印出封閉變數
        var = 'enclosed variable'
        print('在in_func自訂函數內的封閉變數var = ', var)
    in_func( ) 
    print('呼叫in_func自訂函數後的區域變數var = ', var)
var = 'global variable'
print('呼叫out_func自訂函數前的全域變數var = ', var)
out_func( )
print('呼叫out_func自訂函數後的全域變數var = ', var)