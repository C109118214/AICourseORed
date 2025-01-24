# ch7-12.py功能 : 區域變數與全域變數在變數命名空間的查詢
def glo_loc( ):
#glo_loc : 在函數內查詢並印出 y 是否在區域變數在變數命名空間
    y = 6
    print('y in glo_loc = ', ' y ' in locals( ))
x = 3
glo_loc( )
print('y in global = ', ' y ' in globals( ))
print ('x in global = ', ' x ' in globals( ))
# 查詢自訂函數是否為全域變數
print ('glo_loc in global = ', 'glo_loc' in globals( ))