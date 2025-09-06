class Employee:
    language = "python"
    salary = 1200000

harry = Employee()
harry.language = "Javascript"
print(harry.language)

#Here javascript will be printed because instance attribute is given preference over class attributes
