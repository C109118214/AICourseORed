# ch8-23: 銀行綜合存款類別功能
# 定義新增銀行帳戶類別
class createbankaccount:
    # 定義新增帳戶方法，額餘設定為0    
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.balance = 0
    # 定義存款方法 
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    # 定義提款方法          
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
    def __str__(self):
        return('帳號: ' + self.id + '\n姓名: ' + self.name + '\n初期餘額: ' + str(self.balance))
acc0001 = createbankaccount('82262451212', '張曉玲')
acc0002 = createbankaccount('82262741236', '趙子龍')
print(acc0001.__str__( ))
print('存款後餘額: ', acc0001.deposit(10000))
print(acc0002.__str__( ))
print('存款後餘額: ', acc0002.deposit(5000))
print(acc0001.__str__( ))
print('提款後餘額: ', acc0001.withdraw(1000))
print(acc0002.__str__( ))
print('提款後餘額: ', acc0002.withdraw(1000))