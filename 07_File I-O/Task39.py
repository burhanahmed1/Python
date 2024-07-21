'''
The game() function in a program lets a user play a game and returns the score 
as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or 
contains the previous Hi-score. You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.

'''
import random

def game():
    print("Your game starts now.")
    score=random.randint(1,100)
    
    with open("Hi-Score.txt","r") as r:
        hiscore=r.read()
        if(hiscore!=""):
            hiscore=int(hiscore)
        else :
            hiscore=0

    print(f"Your score is : {score}")

    with open("Hi-Score.txt","w") as w:
        if(score>hiscore):
            w.write(str(score))
    
    return score

game()
