#A class method is bound to the class and recieves the class as an implicit first argument
class Person:
    name = "Anonymous"
    @classmethod
    def changename(Person,name):  
        Person.name = name 

p1 = Person()
p1.changename("Shreyas Nambiar")
print(p1.name)
#print(person.name) still prints anynomous because name is an instance of the function chnagename    \


#Person.name = name WORKS, Both will show shreyas 

#self.__class__.name = name WORKS


class Marks:
    def __init__(self,phy, chem, math):
        self.phy = phy
        self.math = math
        self.chem = chem

    @property
    def percentage(self):
        return (self.phy + self.chem + self.math) /3
#The percentage of the student is automatically updated when there is a change in the marks (Using the propertymethod)
