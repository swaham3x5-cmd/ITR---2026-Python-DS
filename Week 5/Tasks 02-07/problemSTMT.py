class BankAccount:

    def __init__(self, account_holder, accountNo, balance):
        self.account_holder = account_holder
        self._accountNo = accountNo
        self.__balance = balance
    
    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}. New balance: {self.__balance}")
    
    def Withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient funds.")
            
    def DispAcc_Details(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self._accountNo}")
        print(f"Balance: {self.__balance}")
        
print("Access Account:")
name = input("Enter Name:")
AccNo = int(input("Enter Account Number:"))
CurrentBalance = float(input("Enter Deposited Amount:"))

C1 = BankAccount(name, AccNo, CurrentBalance)

option = int(input("Enter 1 for Deposit, 2 for Withdraw, 3 for Display Account Details: "))

if option == 1:
    C1.deposit(float(input("Enter Amount to Deposit: ")))
elif option == 2:
    C1.Withdraw(float(input("Enter Amount to Withdraw: ")))
elif option == 3:
    C1.DispAcc_Details()
else:
    print("Invalid option!")
