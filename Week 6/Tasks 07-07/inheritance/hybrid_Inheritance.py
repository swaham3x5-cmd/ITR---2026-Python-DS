class Grandparent:
    def func1(self):
        print("Grandparent class function")

class Father(Grandparent):
    def func2(self):
        print("Father class function")
        
class Mother(Grandparent):
    def func3(self):
        print("Mother class function")
        
class Child(Father, Mother):
    def func4(self):
        print("Child class function") 
        
obj = Child()
obj.func1()
obj.func2()
obj.func3()
obj.func4()