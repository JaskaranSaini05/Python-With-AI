class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
            print("withdrawl successfull")
        else:
            print("insufficient balance")
    def display_balance(self):
        print("owner",self.owner)
        print("balance:",self.balance)
            
account = BankAccount("Aman",10000)

account.deposit(500)
account.withdraw(200)
account.display_balance()