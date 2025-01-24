import numpy as np
import matplotlib.pyplot as plt
x = np.arange( 0, 2.5, 0.1 )
plt.plot( x, x, "-bo", linewidth=1.5,  label = "Linear" )
plt.plot( x, x ** 2, "-mv", linewidth=0.5, markersize = 5, label = "Quadratic" )
plt.plot( x, x ** 3, "-r<", linewidth=0.5, markersize = 4, label = "Cubic" )
plt.xlabel( "x label" ) #x軸標題
plt.ylabel( "y label" ) #y軸標題
plt.title( "Linear plot" ) #圖標題
plt.legend() # 圖例