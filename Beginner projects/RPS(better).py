#This a better, more concise version of the rock paper scissors game with modularization and refactoring.
#REFACTORING: changing the structure of the code without changing its functionality

import random as r 
dict = {
    1 : 'rock',
    2 : 'paper',
    3 : 'scissors'
}
def get_user_choice():
    while True:
        choice = (1,2,3)
        user_choice = int(input("Enter 1 for rock, 2 for paper, 3 for scissors 4 to exit: "))
        if user_choice in choice:
            return user_choice
        elif user_choice == 4:
            print("Thanks for playing the game")
            break
        else:
            print("Invalid input")
            continue
    


def display_choices(user_choice, comp):
    print(f'Your choice: {dict[user_choice]}')
    print(f'Computers choice: {dict[comp]}')


def determine_winner(user_choice, comp):
   if (user_choice == comp):
       print("It's a draw")
   elif (user_choice == 1 and comp ==3 ) or (user_choice == 2 and comp == 1 ) or (user_choice ==3 and comp ==2):
       print("You win")
   elif (user_choice ==1 and comp ==2) or (user_choice ==2 and comp == 1) or (user_choice ==3 and comp ==1 ):
       print("You lose")

def play_game():
    while True:
        user_choice = get_user_choice()
        if user_choice == None: break
        comp = r.randint(1,3)

        display_choices(user_choice, comp)
        determine_winner(user_choice,comp)
        
play_game()