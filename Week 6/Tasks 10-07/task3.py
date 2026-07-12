### Q3.
# Define a class Superman with a method fly().
class Superman:
    def fly(self):
        print("Flying!")
        
def lift_off(obj):
    obj.fly()
    
# Create an object of Superman and pass it to the lift_off() function.
obj = Superman()

lift_off(obj)