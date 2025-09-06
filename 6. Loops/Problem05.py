#Write a program to find out the factorial 

product = 1


number = int(input("Enter the number: "))

for i in range(1,number +1):
    product = product * i 

print(f'The factorial of {number} is {product}')
