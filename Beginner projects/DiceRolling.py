#Problem : code a dice rolling game that takes y/n input from the user and rolls the dice. Any other imput will print as invalid and this should go on untill the user enters n, after that the program terminates


import random as r
n1 = r.randint(1,6)
n2 = r.randint(1,6)  
while True:
    #For an input to be iterated, it should be in the while loop, if the statement is outside, it is forever constant and the condition to break the while loop will be never met. Hence the loop will go on for infinity. If the loop doesnt break, the user is placed with the intial choices again after the execution of the code block.
    user = input("Enter y to roll the dice, n to exit: ")

    if user == 'y':
        print(f'({n1},{n2})')
    elif user == 'n':
        print("Thanks for playing")
        break
    else:
        print("Invalid choice")

