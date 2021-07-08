class BankAccount:

    def __init__(self, int_rate = .02, balance = 0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance < 0:
            print("Insufficient funds: $5 fee")
            self.balance -=  5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(self.balance)
        return self

    def yield_interest(self):
        self.balance += self.int_rate * self.balance
        return self

account1 = BankAccount(.02,1000)
account2 = BankAccount(.02,2000)
account1.deposit(100).deposit(200).deposit(300).withdraw(50).yield_interest().display_account_info()
account2.deposit(200).deposit(50).withdraw(1200).withdraw(500).withdraw(250).withdraw(175).yield_interest().display_account_info()

    
    




