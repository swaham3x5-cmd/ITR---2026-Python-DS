class Mother:
    def func1(self):
        print("Mother class function")

class Father:
    def func2(self):
        print("Father class function")
        
class Child(Mother, Father):
    def func3(self):
        print("Child class function")

obj = Child()

obj.func1()
obj.func2()
obj.func3()