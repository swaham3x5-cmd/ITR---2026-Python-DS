class Grandfather:
    def func1(self):
        print("Grandfather class function")

class Father(Grandfather):
    def func2(self):
        print("Father class function")
        
class Child(Father):
    def func3(self):
        print("Child class function")

obj = Child()

obj.func1()
obj.func2()
obj.func3()