class Book:
    shelves = 5  # class variable
    def __init__(self,title):
        self.title = title  # instance variable

Book1 = Book("Python 101")
Book2 = Book("Java Basics")

print(f"Books {Book1.title} and {Book2.title}")
print(f"Sheleves of books {Book.shelves}")