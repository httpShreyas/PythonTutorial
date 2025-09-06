''''Write a program to print the following star pattern
                * 
                ***
                ***** '''
                
i = 1 
numbers = []
while i < 50:
    numbers.append(i)
    i += 2


for n in numbers:
    print("*" * int(n))
