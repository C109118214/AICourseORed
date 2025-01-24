import numpy as np
F = np.array( [ [ 56, 70 ], [ 25, 75 ] ] )
print( F )

print( np.linalg.det( F ) ) #計算二階行列式

G = np.array( [ [ 123, 20, 142 ],[ 6, 1, 7 ], [ 304, 50, 358 ] ] )
print( G )

print( np.linalg.det( G ) ) #計算三階行列式

I_A = np.array( [ [ 1, -1, -2 ], [ 2, -3, -5 ], [ -1, 3, 5 ] ] )
print( I_A )

I_B = np.array( [ [ 0, 1, 1 ], [ 5, -3, -1 ], [ -3, 2, 1 ] ] )
print( I_B )

Inv_A = np.round( np.linalg.inv( I_A ) )
print( Inv_A )

print( I_A.dot( I_B ) )

E_A1 = np.array( [ [ 2, 3 ], [ 1, 3 ] ] )
E_B1 = np.array( [ 5, 3 ] )
Inv_A1 = np.linalg.inv( E_A1 )
X1 = Inv_A1.dot( E_B1 )
print( X1 )

E_A2= np.array( [ [ 1, -2, 1 ], [ 2, -5, 2 ], [ 3, 1, -1 ] ] )
E_B2 = np.array( [ 7, 6, 1 ] )
Inv_A2 = np.linalg.inv( E_A2 )
X2 = Inv_A2.dot( E_B2 )
print( X2 )