class User:
    bank_name = "First National Dojo"
    
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self,amount):
        self.account_balance -= amount

    def transfer_money(self,amount):
        self.account_balance -= amount

    def receive_money(self, amount):
        self.account_balance += amount

    def display_user_balance(self):
        print(self.acccount_balance)

michael = User("Michael","michael@codingdojo.com")
anna = User("Anna", "anna@hotmail.com")
anna = User()
anna.bank_name = "Dojo Credit Union"
adam = User("Adam Horowitz","adam@beastiemail.com")
michael.make_deposit(100)
michael.make_deposit(200)
michael.make_deposit(300)
michael.make_withdrawal(50)
anna.make_deposit(500)
anna.make_deposit(500)
anna.make_withdrawal(75)
anna.make_withdrawal(75)
anna.receive_money(350)
adam.transfer_money(350)
adam.make_deposit(1900)
adam.make_withdrawal(350)
adam.make_withdrawal(450)
adam.make_withdrawal(150)

print(anna.bank_name)

print(anna.account_balance)
print(adam.account_balance)
print(michael.account_balance)
print(michael.bank_name)




