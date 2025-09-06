'''
class Employee:
    language = "python"
    salary = 1200000
    def getinfo():
    print(f'The language is {language} and the salary is {salary})

harry = Employee()
harry.language = "Javascript"
harry.getinfo() >>>> This line of code gives an error because the computer sees this as:
Employee.getinfo(harry)
'''


'''
class Employee:
    language = "python"
    salary = 1200000
    def getinfo():
    print(f'The language is {self.language} and the salary is {self.salary})

harry = Employee()
harry.language = "Javascript"
harry.getinfo() AND Employee.getinfo(harry) BOTH work 

Output.. 
The language is javascript and the salary is 120000'''



class Greetings:
    def greet(self):
        print("good morning", self)


name =" shreyas"
Greetings.greet("shreyas")


 #@staticmethod is used to specify that a particulat object does not take any arguments
'''
DETAILED EXPLANATION
'''