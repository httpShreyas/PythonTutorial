#The internal processes have been hidden and the user can only see the car's status. This is called abstraction
class Car: 
    def __init__(self):
        self.clutch = False
        self.acc = False
        self.brake = False
    
    def start(self):
        self.clutch = True 
        self.acc = True 
        print("Car has been started.")

audi = Car()
audi.start()

