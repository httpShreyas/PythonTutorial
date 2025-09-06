class Employee: 
    language = "Python"
    salary = 1200000

    def getinfo(self):
        print(f'The salary is {self.salary} and the language is {self.language}')

    @staticmethod
    def greet():
        print("Good morning")

    def __init__(self, name , salary, language):
        #This is a dunder method which is automatically called.
        self.name = name
        self.salary = salary 
        self.language = language
        print("I am creating an object")


shreyas = Employee("shreyas", 323200, "Python")
shreyas.name = "shreyas"
print(shreyas.language, shreyas.salary)


rohan = Employee("rohan", 120000000, "typescriipt")
print(rohan.name, rohan.salary,rohan.language)

