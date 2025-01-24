# ch7-16.py功能: 自訂函數名稱與 Python 內建函數相同
def callfunc(recchar):
# callfunc: 印出標題以及呼叫封閉函數
    print('在callfunc( )函數內')
    num = len(recchar)
    print('char變數內的元素個數 = ', num)
def len(recchar):
# len: 計算字串長度
    sumi = 0
    for i in recchar :
        sumi += 1
    return(sumi)
callfunc('I love Python')