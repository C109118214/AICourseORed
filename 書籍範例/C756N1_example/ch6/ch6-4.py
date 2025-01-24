import numpy as np
Gen_Zero= np.zeros( ( 3, 4 ) )
print( Gen_Zero )

Gen_One = np.ones((3, 4))
print( Gen_One )

Gen_Eye = np.eye((3), dtype = int)
print( Gen_Eye )

Gen_Arange_1 = np.arange(1, 11)
print( Gen_Arange_1 )

Gen_Arange_2 = np.arange( 0.1, 1.1, 0.1 )
print( Gen_Arange_2 )

Gen_Linspace = np.linspace(1, 5, 6)
print( Gen_Linspace )

Rand_Int = np.random.randint( 1, 10, size = 12 )
print( Rand_Int )

np.random.shuffle( Rand_Int )
print( Rand_Int )

Rand_Int = np.random.randint( 1, 10, size = [ 2, 10 ] )
print( Rand_Int )

Rand_Perm = np.random.permutation( 10 ) + 1
print( Rand_Perm )

Rand_Choice1 = np.random.choice( 6, 3, replace = True )
print( Rand_Choice1 )

Rand_Choice2 = np.random.choice( 6, 3, replace = False )
print( Rand_Choice2 )

Rand_Rand = np.random.rand( 3 )
print( Rand_Rand )