class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod #A decorator that works at a class level. It does not use the self parameter . It cannot access or modify class state and generally for utility. Does not access instance attributes
    def start():
        print("The car has been started.")

    @staticmethod
    def stop():
        print("The car has been stopped.")

class Toyota(Car): #The class toyota inherits its properties from the car class
    def __init__(self, name, type):
        self.name = name 
        self.type = type
        
#OBjective: changing the type in the parent class constructor 
        super().__init__(type)
        #Super method super() is used to acces the method of the parent classes. 
        

class Supra(Toyota):
    def __init__(self, price):
        self.price = price

car1 = Toyota("Prius","electric")
print(car1.type)


