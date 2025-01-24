import numpy as np
import matplotlib.pyplot as plt

bins = 100 #設定直方圖的組數
data =  np.random.randn( 10000 )
plt.hist( data, bins, color="green" )

sigma = 2.5
mu = 3
bins = 100
Rand_Mu = sigma * np.random.randn( 10000 ) + mu
plt.hist( Rand_Mu, bins, color='red' )