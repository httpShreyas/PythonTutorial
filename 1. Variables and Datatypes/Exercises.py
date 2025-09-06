#Write a python program to calculate the square of a given number 

number = int(input("Enter your number here: "))
result = number * number
print(result)

print("-"*30)

#Write a python program to find average of 2 nos

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

answer = (num1 + num2) / 2 
print(answer)
print("-"*30)

#Check the type of variable using input function

input1 = input(">: ")
type_of_var = type(input1)
print(type_of_var)

print("-"*30)

#Compare the values of two numbers using boolean
num3 = int(input("Enter your number a here: "))
num4 = int(input("Enter your number b here: "))
 

print("a is greater than b is ", num3 > num4)