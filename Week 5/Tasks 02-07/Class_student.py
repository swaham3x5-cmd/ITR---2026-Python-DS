class Student:
    def __init__(self, name, roll_no, m1, m2, m3):
        self.name = name
        self.roll_no = roll_no
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    
    def cal_Per(self):
        return (((self.m1 + self.m2 + self.m3) / 300) * 100)
    
    def show_info(self):
        print(f"Name : {self.name} \nRoll No : {self.roll_no} \nPercentage : {self.cal_Per()}%")

# input     
name = input("Enter Name:")
roll_no = int(input("Enter Roll no.:"))
m1 = int(input("Enter Marks of Subject 1:"))
m2 = int(input("Enter Marks of Subject 2:"))
m3 = int(input("Enter Marks of Subject 3:"))

if m1 > 100 or m2 >100 or m3 >100:
    print("Invalid Marks")
else:    
    # Object Creation
    s1 = Student(name, roll_no, m1, m2, m3)

    # Display Student Information
    print("\nStudent Information : ")
    s1.show_info()
    
    