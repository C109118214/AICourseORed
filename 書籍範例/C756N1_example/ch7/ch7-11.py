# ch7-11.py 功能: 全域變數與區塊變數同名為不同變數
def var_infunc( ):
# var_infunc 的功能: 在自訂函數內印出x
    x = 5
    print('x = %d% s, obj_id = %d' % (x, 'in var_infunc', id(x)))
x = 10
print('x = %d%s, obj_id = %d' % (x, 'in global', id(x)))
var_infunc( )