# Q1 and Q2
class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}. New balance: {self.__balance}")

    # Q1: Add withdraw method
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient funds!")

# Object Initialization and function calling.
account1 = BankAccount(1000)

account1.deposit(500)

account1.withdraw(300)  # Withdral Successful
account1.withdraw(1500)  # Should show insufficient funds

# Q2: Try to access __balance from outside
print(account1.__balance)