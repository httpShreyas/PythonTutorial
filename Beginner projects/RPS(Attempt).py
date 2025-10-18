#Code a rock paper scissor game where the computer has a random choice and the user is given three options, after the game, print both the users and computers choice and tell whether the user won or lost. The user must have an option to continue the game. 



#CORRECTIONS: 
#The code works, takes the imput and displays the desired output, but it is very repetittive and leads to wastage of space



import random as r 
dict = {
    1 : 'rock',
    2 : 'paper',
    3 : 'scissors'
}


while True:
    try:
      user = int(input("Enter 1 for rock 2 for paper, 3 for scissors and 4 to exit the game:"))
    except ValueError:
        print("Please only enter numbers")
    
    
    computer = r.randint(1,3)
    if user == computer:
        print(f'Draw, You chose: {dict[user]}, Computer chose {dict[computer]}')
    elif user == 1 and computer == 2:
        print(f"You lose, You chose: {dict[user]}, Computer chose {dict[computer]} ")
    elif user == 1 and computer == 3:
        print(f"You win,  You chose: {dict[user]}, Computer chose {dict[computer]}")#No need to display the choices in every if or elif statement. Because these are the constants.
    elif user ==2 and computer ==1:
        print(f'You win  You chose: {dict[user]}, Computer chose {dict[computer]}')
    elif user == 2 and computer ==3:
        print(f'You lose,  You chose: {dict[user]}, Computer chose {dict[computer]}')
    elif user == 3 and computer == 1:
        print(f'You lose  You chose: {dict[user]}, Computer chose {dict[computer]}')
    elif user == 3 and computer == 2:
        print(f'you win,  You chose: {dict[user]}, Computer chose {dict[computer]}')
    elif user == 4:
        break
    else: print("invalid input")
    