import numpy as np
ary =np.array( [ 12, 31, 25, 45 ] ) 
N = len( ary )
for i in range( N - 1 ): 
    for j in range( N - i - 1 ): 
        if ary[ j ] < ary[ j + 1 ]:  
            #將ary[ j ] 與 ary[ j + 1 ]互換值 
            ary[ j ], ary[ j + 1 ] = ary[ j + 1 ], ary[ j ]  
            #將陣列轉成字串，指定 %s 格式化輸出
    print( "%s%d%s%s" % ( "步驟", i + 1, ". ary陣列 = ", str( ary ) ) )