class BankAccount:
    
    def __init__(self, account_holder, account_no, balance=0.0):
        self.account_holder = account_holder
        self._account_no = account_no
        self.__balance = balance  # Private balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"✅ Deposited ₹{amount:,.2f}. New balance: ₹{self.__balance:,.2f}")
        else:
            print("❌ Invalid amount. Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("❌ Invalid amount. Withdrawal amount must be positive.")
        elif amount > self.__balance:
            print("❌ Insufficient funds!")
            print(f"   Current balance: ₹{self.__balance:,.2f}")
        else:
            self.__balance -= amount
            print(f"✅ Withdrew ₹{amount:,.2f}. New balance: ₹{self.__balance:,.2f}")

    def display_details(self):
        print("\n" + "="*40)
        print("          ACCOUNT DETAILS")
        print("="*40)
        print(f"Account Holder : {self.account_holder}")
        print(f"Account Number : {self._account_no}")
        print(f"Current Balance: ₹{self.__balance:,.2f}")
        print("="*40)

    def get_balance(self):
        return self.__balance


# ==================== REAL BANK COUNTER ====================

print("🏦 Welcome to Python Bank Counter 🏦\n")

# Account Creation
name = input("Enter Account Holder Name: ").strip()
while not name:
    print("Name cannot be empty!")
    name = input("Enter Account Holder Name: ").strip()

acc_no = input("Enter Account Number: ").strip()
while not acc_no.isdigit():
    print("Please enter a valid account number (digits only)!")
    acc_no = input("Enter Account Number: ").strip()

initial_balance = float(input("Enter Initial Deposit Amount (₹): ") or 0)

# Create account
account = BankAccount(name, int(acc_no), initial_balance)
print(f"\n✅ Account created successfully for {name}!\n")

# Main Banking Loop (Real Counter Experience)
while True:
    print("\n" + "-"*50)
    print("🏧 BANK COUNTER MENU")
    print("-"*50)
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance / Account Details")
    print("4. Exit")
    print("-"*50)

    try:
        option = int(input("\nEnter your choice (1-4): "))

        if option == 1:
            amt = float(input("Enter amount to deposit (₹): "))
            account.deposit(amt)

        elif option == 2:
            amt = float(input("Enter amount to withdraw (₹): "))
            account.withdraw(amt)

        elif option == 3:
            account.display_details()

        elif option == 4:
            print("\nThank you for banking with us! Have a great day! 👋")
            break

        else:
            print("❌ Invalid option! Please choose 1-4.")

    except ValueError:
        print("❌ Please enter a valid number!")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

print("\nSession ended.")