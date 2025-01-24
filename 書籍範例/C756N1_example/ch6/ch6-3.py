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