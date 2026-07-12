class Person:       # Base Class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, roll_no, course, marks):
        Person.__init__(self, name, age)
        self.roll_no = roll_no
        self._course = course
        self.__marks = marks
        
    def setMarks(self, marks):
        self.__marks = marks
    
    def getMarks(self):
        return self.__marks
    
    def display(self):
        Person.display(self)
        print(f"Roll No: {self.roll_no}")
        print(f"Course: {self._course}")
        print(f"Marks: {self.getMarks()}")


class SportsStudent(Student):
    def __init__(self, name, age, roll_no, course, marks, sport_name):
        Student.__init__(self, name, age, roll_no, course, marks)
        self.sport_name = sport_name
        
    def display(self):
        Student.display(self)
        print(f"Sport Name: {self.sport_name}")


class Result:
    def calculate_Student_Marks(self, student):
        marks = student.getMarks()
        total_marks = marks
        avg_marks = marks
        
        print(f"Total Marks of Student: {int(total_marks)}")
        print(f"Average Marks of Student: {int(avg_marks)}")

        if avg_marks >= 90 and avg_marks <= 100:
            print("Grade A")
        elif avg_marks >= 80 and avg_marks < 90:
            print("Grade B")
        elif avg_marks >= 70 and avg_marks < 80:
            print("Grade C")
        elif avg_marks >= 60 and avg_marks < 70:
            print("Grade D")
        elif avg_marks >= 50 and avg_marks < 60:
            print("Grade E")
        elif avg_marks >= 40 and avg_marks < 50:
            print("Grade F")
        else:
            print("Fail")

# Display Method
def display_info(student):
    student.display()

print("=== Student Management System ===")
# Regular Student
print("\n--- Regular Student ---")
stud1 = Student("Swaham", 18, 45, "Computer Science", 81)
stud1.display()

print("\nUsing Getter/Setter:")
stud1.setMarks(85)
print("Updated Marks:", stud1.getMarks())

# Sports Student
print("\n--- Sports Student ---")
sport_stud = SportsStudent("Rajas", 20, 50, "Physics", 92, "Cricket")
sport_stud.display()

# Result
print("\n--- Result for Regular Student ---")
result = Result()
result.calculate_Student_Marks(stud1)

print("\n--- Result for Sports Student ---")
result.calculate_Student_Marks(sport_stud)

# Display
print("\n--- Different Display Calls ---")
print("1. Regular Display:")
display_info(stud1)

print("\n2. Sports Display:")
display_info(sport_stud)