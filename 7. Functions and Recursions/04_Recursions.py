#Recursion: It is a function that calls itself.
'''
factorial(n) = n x n-1 x .... 3x2x1
factorial(n) = n x factorial(n-1)'''


def factorial(n):
    if n == 0 or n == 1:
        return 1 
    return n * factorial(n-1)

n = int(input("Enter a number: "))
print(f'The factorial of the given number is {factorial(n)}')


#This function resolves the given equation untill the factorial of 1 is reached.
#The function should not infinitely call itself
