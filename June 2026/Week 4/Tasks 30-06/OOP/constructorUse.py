class Student:
    def set_name(self,name):
        self.name = name
    def say_hello(self):
        print(f"Hello! I'm a student named {self.name}")
        
s1 = Student()
s1.set_name("Swaham")
s1.say_hello()