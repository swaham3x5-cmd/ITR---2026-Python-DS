# Create a "Library" class with a private "__books" attribute and methods to issue and return books.

import pandas as pd
class Library:
    def __init__(self, books, status):
        self.__books = books
        self.status = status
    def issue_book(self, book_name, status):
        
        if book_name in self.__books and status == "available":
            self.status = "issued"
            print(f"The book '{book_name}' has been issued.")
        else:
            print(f"The book '{book_name}' is not available.")

    def return_book(self, book_name, status):
        if book_name in self.__books and self.status == "issued":
            self.status = "available"
            print(f"The book '{book_name}' has been returned.")
        else:
            print(f"This {book_name} isn't from this library.")

Library_Data = pd.read_csv("Books_data.csv")

library = Library(Library_Data["title"].tolist(), Library_Data["status"].tolist())

option = 0

while True:
    option = int(input("Enter 1 to issue a book or 2 to return a book:"))
    
    try:
        if option == 1:
            book_name = input("Enter the name of the book you want to issue:")
            library.issue_book(book_name, Library_Data.loc[Library_Data["title"] == book_name, "status"])
        elif option == 2:
            book_name = input("Enter the name of the book you want to return:")
            library.return_book(book_name, Library_Data.loc[Library_Data["title"] == book_name, "status"])        
        elif option == 3:
            print("Have a nice day!")
            break
        else:
            print("Invalid option. Please enter valid option.")
    except ValueError:
        print("Invalid Option")