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

print( Gen_S )

Gen_T = np.array( [ [ 3, 5, 2, 6, 4 ], [ 82, 86, 68, 89, 92 ] ] )
print( Gen_T )

Gen_H = np.hstack( ( Gen_S, Gen_T ) )
print( Gen_H )

Gen_V = np.vstack( ( Gen_S, Gen_T ) )
print( Gen_V )

Gen_P = Gen_V[ 1 : : 2, : ]  #取出Gen_V陣列所有行，第 1 列到最後 ( 遞增2 )
print( "Gen_P 排序前 = ", Gen_P )

print( "Gen_P 排序後(列) = ", np.sort( Gen_P, axis = 0 ) ) #按列排序

Gen_Trans = np.transpose( Gen_P ) #Gen_P陣列由行轉列
print( Gen_Trans )

print( "Gen_P轉置後平均(行) =", np.mean( Gen_Trans, axis = 0 ) )