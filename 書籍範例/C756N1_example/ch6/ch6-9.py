import numpy as np
A = np.array( [ [ 6, 3, 1 ], [ 5, 2, 4 ], [ 5, 1, 4 ] ] )
print( A )

B = np.array( [ [ 2, 4, 6 ], [ 1, 3, 5 ], [ 3, 5, 7 ] ] )
print( B )

C = A + B
print( C )

D = A * B
print( D )

E = B ** 2
print( E )

print( np.log( E ) )

print( np.sqrt( E ) )

print( np.sum( E ) )

print( np.mean( E ) )

print( np.max( E ) )