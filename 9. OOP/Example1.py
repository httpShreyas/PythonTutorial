class Student:
    def __init__(self,name,eng,math,science):
        self.eng = eng
        self.math = math 
        self.science = science 
        self.name = name 
        
    def average(self):
      return ((self.eng + self.math + self.science)/3)

shreyas = Student("shreyas",10,10,10)
avg = shreyas.average()
print(avg)