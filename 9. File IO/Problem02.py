'''
IMP: 
The game function in a program lets a user play a game and returns the score as an integer> 
You nee to read a file "Highscore.txt which is either blank or contains the previous high score. 
Write a program to update the text file whenever the highscore gets broken.'''


import random

def game(): 
    score = random.randint(1,50)
    with open("Highscore.txt") as f:
        hiscore = f.read()
        if hiscore != "":
            hiscore = int(hiscore)
        else:
            hiscore = 0 


    print(f'Your score is {score}')
    if score > hiscore:
        with open("Highscore.txt", "w") as f:
            f.write(str(score))

  
    return score

game()