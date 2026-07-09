class Vehicle:
    def start(self):
        print("Starting...")

class Car(Vehicle):
    def drive(self):
        print("Driving...")
        
obj = Car()
obj.start()
obj.drive()