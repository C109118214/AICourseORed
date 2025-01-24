import numpy as np
import matplotlib.pyplot as plt
N = 500  #設定樣本數
x = np.random.randn( N )
y = np.random.randn( N )
color = np.random.randn( N )
plt.scatter( x, y, c = color )
plt.axis( [ -4, 4, -4, 4 ] )
plt.title( "Scatter plot" )
plt.xlabel( "x" )
plt.ylabel( "y" )
plt.colorbar() #顯示色標