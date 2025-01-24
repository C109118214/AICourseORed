import numpy as np
import matplotlib.pyplot as plt
x = np.linspace( 3 * -np.pi, 3 * np.pi, 300 )
print( x )

y = 2 * np.sin( x )
print( y )

plt.plot( x, y, "bo", markersize = 2 )
plt.xlabel( "x" ) #x軸標題
plt.ylabel( "y" ) #y軸標題
plt.title( "y = 2 * sin x" ) #圖標題

y1 = np.cos( x )
plt.plot( x, y1, "r+", markersize = 2, label = "sin x" )
y2  = np.sin( x )
plt.plot( x, y2, "bo", markersize = 2, label = "cos x" )
plt.xlabel( "x" ) #x軸標題
plt.ylabel( "y" ) #y軸標題
plt.title( "sin x cross cos x" ) #圖標題
plt.legend() # 圖例

x = np.linspace( -1.3, 1.3, 80 )
y3 = np.tan( x )
plt.plot( x, y3, "bx", markersize = 3 )
plt.xlabel( "x" ) #x軸標題
plt.ylabel( "y" ) #y軸標題
plt.title( "y = tan x" ) #圖標題

