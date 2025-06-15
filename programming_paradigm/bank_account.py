class BankAccount:
    def __init__(self,balance=0):
        self.account_balance=balance
    def deposit(self,amount):
        if amount>0:
            self.account_balance+=amount
        else:
            print("amount must be positive")
    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
          self.account_balance -= amount
          print(f"Withdrew: ${amount:.1f}")
          return True
        else:
          print("Insufficient funds.")
          return False
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.1f} ")