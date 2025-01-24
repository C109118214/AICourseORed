import numpy as np
import matplotlib.pyplot as plt
x =  np.arange( 10 ) + 1 
y =  np.random.randint( 60, 100, size = 10 )
print( x, y )
plt.bar( x, y, color = "blue" )