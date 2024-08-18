"""
Part 1: Introduction to the Base Class
Understanding BankAccount:

Task: Create a base class called BankAccount with the following attributes and methods:

Attributes:
balance: The initial amount of money in the account.
name: The name of the account.

Methods:
get_balance: Print the current balance.
deposit: Add a specified amount to the balance.
withdraw: Subtract a specified amount from the balance if sufficient funds are available.
transfer: Transfer a specified amount to another account.
"""


class BankAccount:
    def __init__(self, balance, name):
        self.balance = balance
        self.name = name

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            return "Insufficient funds"

    def transfer(self, amount, account):
        if amount <= self.balance:
            self.balance -= amount
            account.balance += amount
        else:
            return "Insufficient funds"

# PART 2:
class InterestAccount(BankAccount):
    def __init__(self, balance, name):
        super().__init__(balance, name)

    def deposit(self,amount):
        super().deposit((amount+ amount * 0.05))
        

# PART 3:
class SavingsAccount(BankAccount):
    def __init__(self, balance, name):
        super().__init__(balance, name)

    def deposit(self,amount):
        super().deposit((amount+ amount * 0.05))

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= (amount + amount * 0.05)
        else:
            return "Insufficient funds"

    def transfer(self, amount, account):
        if amount <= self.balance:
            self.balance -= amount
            account.balance += amount
        else:
            return "Insufficient funds"



amjad = BankAccount(1000, "Amjad")
sara = BankAccount(2000, "Sara")

print("Starting balance")
print(amjad.name , "Starting balance",amjad.get_balance())
print(sara.name , "Starting balance",sara.get_balance())

depositAmount = 500
print(f"== Deposit == {depositAmount} to", amjad.name)
amjad.deposit(500)
print(amjad.name , "balance after depositing ",amjad.get_balance())

# withdrawl more than balance amount from sarah
withdrawAmount = 3000
print(f"== Withdraw == {withdrawAmount} from", sara.name)
print(sara.withdraw(3000))

# withdrawl less than balance amount from sarah
withdrawAmount = 500
print(f"== Withdraw == {withdrawAmount} from", sara.name)
sara.withdraw(500)
print(sara.name , "balance after withdrawing ",sara.get_balance())


####  PART 2 ####
# Every InterestRewardsAcct user always receive 5% reward on adding more money

print("Starting balance")
print(sara.name , "Starting balance",amjad.get_balance())

sara2 = InterestAccount(2000, "Sara")
sara2.deposit(500)
print(sara2.name , "Interest deposited balance",sara2.get_balance())


sara3 = SavingsAccount(2000, "Sara")
sara3.deposit(500)
print(sara3.name , "Savings deposited balance",sara3.get_balance())
sara3.withdraw(1000)
print(sara3.name , "Savings withdraw balance",sara3.get_balance())

sara3.transfer(500, amjad)
print(sara3.name , "Savings transfer balance",sara3.get_balance())
print(amjad.name , "Savings transfer balance",amjad.get_balance())

