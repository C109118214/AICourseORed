import numpy as np
ary = np.array( [ 1, 2, 5, 7, 8, 10, 13, 18 ] ) 
N = len( ary )
x = 10
for i in range( N ): 
    if ary[ i ] == x:
        print( "%s%d%s%d%s" % ( "目標值 ",x ," 是在陣列的第 ",i+1," 個位置" ) )