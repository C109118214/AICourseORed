# ch8-19: Raise 引發異常
import math
try: 
    mypi = '3.1416'
    result = math.sqrt(mypi)
    raise TypeError 
except TypeError as e: 
    print('字串不能算術運算: ' + str(e))  
    result = math.sqrt(float(mypi))
    print('pi 開根號 = ', result)