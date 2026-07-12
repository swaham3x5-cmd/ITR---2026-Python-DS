class Parent:
    def func1(self):
        print("Parent class function")

class Child(Parent):
    def func2(self):
        print("Child class function")

obj = Child()

obj.func1()
obj.func2()