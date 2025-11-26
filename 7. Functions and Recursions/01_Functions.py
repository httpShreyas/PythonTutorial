#Functions are group of statements performing a specefic task

#Example: using a fuction to calculate average:

#This is called as the function definition 
def avg():
    a =  int(input("Enter your number:"))
    b =  int(input("Enter your number:"))
    c =  int(input("Enter your number:"))
    average = (a+b+c)/3
    print(average)

avg() #This is called a fuction call, it executes the code given in the function