class rectangle:
    
    def __init__(self, len, bre):
        self.len = len
        self.bre = bre
        
    def show(self):
        print(f"Dimensions of Rectangle : {self.len} * {self.bre}")
        
R1 = rectangle(input("Enter Length = "),input("Enter Breadth = "))
R1.show()