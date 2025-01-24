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