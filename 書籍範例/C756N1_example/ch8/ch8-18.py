# ch8-18: 變數名稱錯誤與數值錯誤
print('---變數名稱錯誤---')
x = 5
xx = x ** 2
print('x求平方 = ', xx)
print('---數值錯誤---')
y = '10'
# y = 'NA'
result = xx + int(y)
print('x求平方加y = ', result)