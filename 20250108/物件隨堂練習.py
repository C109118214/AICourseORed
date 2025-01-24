# -*- coding: utf-8 -*-
class deposit:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.amount = 0
    
    def add_money(self, money):
        self.amount+= money
        
    def withdraw(self, money):
        self.amount-= money
    
    def check(self):
        print(self.name, "的帳戶餘額為", self.amount)

account_1 = deposit("Ken", "C001")
account_2 = deposit("Ada", "C002")

account_1.check()
account_1.add_money(10000)
account_1.check()
account_1.withdraw(4000)
account_1.check()

account_2.check()
account_2.add_money(20000)
account_2.check()
account_2.withdraw(3000)
account_2.check()