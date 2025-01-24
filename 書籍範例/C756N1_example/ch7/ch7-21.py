# ch7-21.py 功能: 計算度的三角函數值
import numpy as np
def trigfunc(F, D):
# Trig_Func( ): 代入函數方法計算三角函數值並回傳值與方法
    R_pi = np.pi / 180
    if F == 1:
        value = np.sin(D * R_pi)
        Method = 'sin'
    elif F == 2 :
        value = np.cos(D * R_pi)
        Method = 'cos'
    elif F == 3:
        value = np.tan(D * R_pi)
        Method = 'tan'
    else:
        print('輸入錯誤')
    return(str(value), Method)
Funcs = int(input('請輸入 1.sin 2.cos 3.tan = '))
Degree = int(input('請輸入度數 0, 30, 45, 60, 90, 180, 270 = '))
[value, Method] = trigfunc(Funcs, Degree)
if Funcs == 3 and (Degree == 90 or Degree == 270):
    value = '無意義'
print('%s %d %s%s ' % (Method, Degree, "度的三角函數值 = ", value))