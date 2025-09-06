#python rock paper scissors
import random
def game():
    userinp = input("Enter rock,paper or scissors: ").lowe
    
    dicts = {
        "rock": 1 ,
        "paper": 0 ,
        "scissors": -1
    }

    user = dicts[userinp]
    comp = random.randint(-1,1)


    