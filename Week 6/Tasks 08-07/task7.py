# Q7
class Device:
    def power_on(self):
        print("Device powered on.")

class Phone(Device):
    def call(self):
        print("Making a call.")

class Camera(Device):
    def take_photo(self):
        print("Taking a photo.")

class SmartPhone(Phone, Camera):
    pass  # Multiple inheritance

# Object Initialization and function calling.
sp = SmartPhone()

sp.power_on()
sp.call()
sp.take_photo()