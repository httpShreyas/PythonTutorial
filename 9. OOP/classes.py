class Circle: #Attributes are color height and width
    def __init__(self,radius,color):
        self.radius = radius 
        self.color = color
        #INIT is a constructor,which is used to initialize data attributes
        #SELF: refers to the newly created instance of the class
    def add_radius(self,r): #This is a method added 
            self.radius += r 
class Rectangle:
    def __init__(self, color, height, width):
        self.color = color
        self.height = height
        self.width = width
#AN object is the realization or instantiation of that class

#CREATING AN INSTANCE OF A CLASS
C1 = Circle(10, "red")
# TO change the data 
C1.color = "blue"
C1.add_radius(2)
#DO not care about the self paramater while calling functions
C2 = Circle(10,"blue")

#DIR dir(name of object)>>> Gives the data attributes and methods in a class
