import numpy as np
#引用Gen_1D, Gen_2D, Gen_3D陣列查詢維度與軸
Gen_1D = np.array( [ 6, 3, 1 ] )
Gen_2D = np.array( [ [ 6, 3, 1 ], [ 5, 2, 4 ], [ 5, 1, 4 ] ] )
Gen_3D = np.array( [ [ [ 6, 3, 1 ], [ 5, 2, 4 ],
                        [ 5, 1, 4 ], [ 2, 3, 5 ] ],
                       [ [ 2, 5, 7 ], [ 4, 8, 7 ],
                        [ 4, 9, 2 ], [ 5, 3, 1 ] ] ] )
print( Gen_1D.shape, Gen_2D.shape, Gen_3D.shape )

#引用Gen_1D, Gen_2D, Gen_3D陣列查詢軸
print( Gen_1D.ndim, Gen_2D.ndim, Gen_3D.ndim )

print( Gen_1D[ : ] ) #取出全部的元素

print( Gen_1D[ 1 : 3 ] ) #取出索引1到3的前一個

print( Gen_1D[ : -1 ] )#取出自索引0開始倒數前一個

print( Gen_1D[ : : -1 ] ) #全部反向取出

Gen_S = np.array( [ [ 6, 4, 4, 3, 3 ], [ 80, 76, 78, 88, 62 ] ] )
print( Gen_S )

print( Gen_S[ 0 : 2, 2 : 4] ) #取出0到1列及2到3行

print( Gen_S[ : , : : 3] ) #取出所有列及所有行並取行時遞增3個元素

print( Gen_S[ : 2, 1 : ] ) #取出0到1列及第1行開始到最後

print( Gen_S[ : : -1, : : -1 ] ) #全部反向取出元素