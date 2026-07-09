class Parent:
    def func1(self):
        print("Parent class function")

class Child1(Parent):
    def func2(self):
        print("Child1 class function")
        
class Child2(Parent):
    def func3(self):
        print("Child2 class function")

obj1 = Child1()
obj1.func1()
obj1.func2()

obj2 = Child2()
obj2.func1()
obj2.func3()