x  =  print( 1+2) # add

print(type(x)) #This is an object of the class int and vice versa

print("Shreyas" + "Nambiar") #Concatenate 
#The function of the + operator changes with the 

#When the same operator is allowed to have different meanings according to the context, it is called as polllyorphism

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def shownumber(self):
        print(self.real ,"i +" ,self.imag ,"j")
    
    
n1 = Complex(1,3)
n1.shownumber()

n2 = Complex(2,5)
n2.shownumber()
