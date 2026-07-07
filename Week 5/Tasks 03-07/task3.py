# Write a Python program to implement encapsulation using an "ATM" class with a private "__pin" attribute.

class ATM:
    def __init__(self, pin):
        self.__pin = pin
    
    def pin_check(self, entered_pin):
        if entered_pin == self.__pin:
            print("Welcome to the ATM!")
        else:
            print("PIN doesn't match. Authorization failed!! \n Try again later.")
    
user_pin = int(input("Set your PIN:"))
atm = ATM(user_pin)

entered_pin = int(input("Confirm your PIN :"))

atm.pin_check(entered_pin)