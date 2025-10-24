#A class method is bound to the class and recieves the class as an implicit first argument
class Person:
    name = "Anonymous"

    def changename(self,name):  
        self.name = name 

p1 = Person()
p1.changename("Shreyas Nambiar")
print(p1.name)
#print(person.name) still prints anynomous because name is an instance of the function chnagename    \


#Person.name = name WORKS, Both will show shreyas 

#self.__class__.name = name WORKS

