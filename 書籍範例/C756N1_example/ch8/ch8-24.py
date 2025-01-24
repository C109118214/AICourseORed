# ch8-24: 銀行綜合存款類別功能
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
    # 新增支票帳戶類別繼承自CreateBankAccount類別
class checkingaccount(createbankaccount):
    def __init__(self, id, name):
        super( ).__init__(id, name)   # 呼叫父類別__init__( )
        self.overdraftlimit = 30000   #透支額度
    # 改寫加入透支額度的提款方法         
    def withdraw(self, amount):
        if amount <= self.balance + self.overdraftlimit:
            self.balance -= amount 
        else:
            raise ValueError('超出信用額度')
        return self.balance
    def __str__(self):
        return (super( ).__str__( ) + '\n透支額度\t' + str(self.overdraftlimit));
ckacc0005 = checkingaccount('82270025425', '陳子義')
print(ckacc0005.__str__( ))
print('存款後餘額: ', ckacc0005.deposit(9000))
print('提款後餘額: ', ckacc0005.withdraw(20000))
# print('提款後餘額: ', ckacc0005.withdraw(50000))