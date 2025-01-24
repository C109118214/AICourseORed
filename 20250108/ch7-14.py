# ch7-14. py 功能 : 在自訂函數內將某變數宣告全域變數
def dec_glo( ):
# dec_glo: 在函數內印出全域變數
    global num_var
    num_var = num_var + 10
    print('在dec_glo函數內num_var = ', num_var,' ,id = ', id(num_var))
num_var = 5 
print('呼叫dec_glo函數前, num_var = ', num_var,' , id = ', id(num_var))
dec_glo( )
print('呼叫dec_glo函數後num_var = ', num_var,' ,id = ', id(num_var))