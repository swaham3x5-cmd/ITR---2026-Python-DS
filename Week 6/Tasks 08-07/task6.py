# Q6
class Principal:
    def manage_school(self):
        print("Managing the school.")

class Teacher(Principal):
    def teach(self):
        print("Teacher is teaching.")

class Student(Principal):
    def study(self):
        print("Student is studying.")

# Object Initialization and function calling.
t = Teacher()
s = Student()

t.manage_school()  # Inherited
t.teach()
s.manage_school()  # Inherited
s.study()