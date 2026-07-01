class Student:
    branch = 'CO'
    def __init__(self,name):
        self.name = name
        
S = Student("Swaham")
print(S.name)
print(S.branch)