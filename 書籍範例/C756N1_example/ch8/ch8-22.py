#ch8-22: 定義利率類別加入異常處理
class interestrate:
    # 有效利率方法
    def earfix(self, rn, m):
        # earfix: 計算有效利率公式   
        if m <= 0 | m > 365: 
            raise ValueError('輸入的參數必須介於1到365哦')
        elif type(m) is not int:
            raise TypeError('輸入的參數必須是整數哦')
        else: 
            ear = ((1 + (rn / m)) ** m) - 1
        return(ear)  
# 設定年、半年、季、月、週、日複利的次數    
m = input('輸入複利期數如 1  2  4  12  52  365 = ').split( )
rn = float(input('請輸入年利率(如 0.06) = '))
# 進迴圈依不次期間呼叫類別的方法計算有效利率並偵測錯誤
for i in m:
    try: 
        ir = interestrate( )
        ear = ir.earfix(rn, int(i))
    except ValueError as v:
        print('數值錯誤，' + str(v))
        break 
    except TypeError as t :
        print('型別錯誤，' + str(t))  
        break         
    else: 
        print('年複利次數%4d, 有效利率 = %6.4f%%' %(int(i), ear*100))