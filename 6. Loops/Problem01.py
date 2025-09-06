#Write a program to print the multiplication table of a given number:

number = int(input("Enter the number: "))

multiple = int(input("Enter the multiple: "))

for i in range(1, multiple + 1):
    result = i * number
    final = f'{number} x {i} = {result}'
    print(final)