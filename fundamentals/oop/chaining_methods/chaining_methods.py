class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self,amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(self.account_balance)
        return self 

michael = User("Michael","michael@codingdojo.com")
michael.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(50).display_user_balance()



        

    
