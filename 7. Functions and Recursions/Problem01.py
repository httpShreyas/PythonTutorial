#Write a program using fuctions to find the greatest of three numbers:

def greatest_numbers():
    if a > b and c:
       print(f'{a} is the greatest number')
    elif b > a and c:
         print(f'{b} is the greatest number')
    elif c > a and b:
         print(f'{c} is the greatest number')

        

a = int(input("Enter number: "))
b = int(input("Enter number: "))
c = int(input("Enter number: "))

greatest_numbers()


''' Important:
Correct solution:
Instead of a > b and c we can write >> a>b and a>c 
due to this the fuction wouldnt get confused when two equal numbers are entered'''