import numpy as np
ary =np.array( [5, 8, 2, 6] )
N = len( ary )
for i in range( N - 1 ): 
    min_index = i 
    for j in range( i + 1, N ): 
        if ary[ min_index ] > ary[ j ] :
            min_index = j
    #將ary[ i ] 與 ary[ min_index ] 互換值            
    ary[ i ], ary[ min_index ] = ary[ min_index ], ary[ i ] 
    #將陣列轉成字串，指定 %s 格式化輸出
    print( "%s%d%s%s" % ( "步驟", i + 1, ". ary陣列 = ", str( ary ) ) )