# Create a "Library" class with a private "__books" attribute and methods to issue and return books.

class Library:
    def __init__(self):
        self.__books = ["DBMS", "MIC", "STE", "DCN"]
    
    def issue(self, book):
        
        if book in self.__books:
            self.__books.remove(book)
            print(f"Book '{book}' issued successfully.")
            return True
        
        else:
            print(f"Book '{book}' is not available.")
            return False
    
    def return_book(self, book):

        self.__books.append(book)
        print(f"Book '{book}' returned successfully.")
        return True

lib = Library()
  
while True:
        print("\nOptions:")
        print("1. Issue Book")
        print("2. Return Book")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == "1":
            book = input("Enter book name to issue: ")
            if book:
                lib.issue(book)
        elif choice == "2":
            book = input("Enter book name to return: ")
            if book:
                lib.return_book(book)

        elif choice == "3":
            print("Thank you for using the Library System!")
            break
        else:
            print("Invalid choice! Please enter 1, 2, 3, or 4.")