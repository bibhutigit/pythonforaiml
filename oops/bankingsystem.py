class Bank:
    def __init__(self,user,balance=0):
        self.user = user
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print(f"{amount} is credited in your account. Available balance is {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
        print(f"{amount} is debited from your account. Available balance is {self.balance}")

    def check_balance(self):
        print(f"{self.user}'s balance is {self.balance}")

mybank = Bank("Bibhuti")
mybank.check_balance()

mybank.deposit(50000)
mybank.check_balance()

mybank.withdraw(20000)
mybank.check_balance()