import numpy as np
Gen_1D = np.array( [ 6, 3, 1 ] )
print( "一維陣列 =", Gen_1D  )
print( "一維索引值為 2 的元素 = ", Gen_1D[ 2 ] )

Gen_2D = np.array( [ [ 6, 3, 1 ], [ 5, 2, 4 ], [ 5, 1, 4 ] ] )
print( "二維陣列 =", Gen_2D  )
print( "二維陣列第2列第1到2行的元素 =", Gen_2D[ 2, 1 : 3 ] )

Gen_3D = np.array( [ [ [ 6, 3, 1 ], [ 5, 2, 4 ],
                     [ 5, 1, 4 ], [2, 3, 5 ] ],
                     [ [ 2, 5, 7 ], [ 4, 8, 7 ],
                      [ 4, 9, 2 ], [ 5, 3, 1 ] ] ] )
print( Gen_3D )

print( Gen_3D[ 1, 0, 2 ] )
print( Gen_3D[ 0, 1, 2 ] )
print( Gen_3D[ 0, 3, 0 ] )
print( "陣列內的所有元素 =", Gen_3D.size )
print( "一維陣列的形狀 =", Gen_1D.shape )
print( "二維陣列的形狀 =", Gen_2D.shape )
print( "三維陣列的形狀 =", Gen_3D.shape )
print( Gen_3D.dtype )