# Write a class that meets these requirements.
#
# Name:       BankAccount
#
# Required state:
#    * opening balance, the amount of money in the bank account
#
# Behavior:
#    * get_balance()      # Returns how much is in the bank account
#    * deposit(amount)    # Adds money to the current balance
#    * withdraw(amount)   # Reduces the current balance by amount
#
# Example:
#    account = BankAccount(100)
#
#    print(account.get_balance())  # prints 100
#    account.withdraw(50)
#    print(account.get_balance())  # prints 50
#    account.deposit(120)
#    print(account.get_balance())  # prints 170
#
# There is pseudocode for you to guide you.

# class BankAccount
class BankAccount:
    # method initializer(self, balance)
    def __init__(self, balance):
        # self.balance = balance
        self.balance = balance

    # method get_balance(self)
    def get_balance(self):
        # returns the balance
        return self.balance

    # method withdraw(self, amount)
    def withdraw(self, amount):
        # reduces the balance by the amount
        self.balance -= amount

    # method deposit(self, amount)
    def deposit(self, amount):
        # increases the balance by the amount
        self.balance += amount

account = BankAccount(100)

print(account.get_balance())  # prints 100
account.withdraw(50)
print(account.get_balance())  # prints 50
account.deposit(120)
print(account.get_balance())  # prints 170
