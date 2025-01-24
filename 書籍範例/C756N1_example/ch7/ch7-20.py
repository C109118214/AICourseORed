# ch7-20.py 功能: 聯立方程式自訂函數
import numpy as np
def binlinprog(A, B):
# BinLinProg( ):代入 A , B 係數陣列計算聯立方程式解
    Inv_A1 = np.linalg.inv(A)
    X1 = Inv_A1.dot(B)
    return X1
# A輸入2 3 1 3 ，B輸入5 3
E_A1 = np.fromstring(input('請輸入A係數矩陣 = '), dtype = int, sep = ' ')
E_A1 = E_A1.reshape(2, 2)
E_B1 = np.fromstring(input('請輸入B係數矩陣 = '), dtype = int, sep = ' ')
print('A係數陣列 = ', E_A1)
print('B係數陣列 = ', E_B1)
Ans = binlinprog(E_A1, E_B1)
print('聯立方程式解 = ', Ans)