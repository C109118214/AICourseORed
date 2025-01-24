import numpy as np
ary =np.array( [ 1, 2, 5, 7, 8, 10, 13, 18, 34, 55 ] ) 
x = 5
N = len( ary )
low = 0
high = N - 1
found = False
while ( found == False ) & ( low <= high ):
    mid = ( low + high ) // 2
    if ary[ mid ] == x:  #條件1
        found = True
        print( "%s%d%s%d%s" % ( "目標值 = ", x, ",在陣列第 ", mid + 1, " 個位置" ) )
    elif x < ary[ mid ] :  #條件2
        high = mid - 1
    else:   #以上條件均不滿足
        low = mid + 1 
if found == False:
    print( "目標值沒有找到" )