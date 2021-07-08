class User:
    bank_name = "First National Dojo"
    
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self):
        self.account.deposit(100)

    def make_withdrawal(self):
        self.account.withdrawal(50)

    def display_user_balance(self):
        print(self.acccount.balance)
    
