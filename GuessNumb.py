#THIS IS ACTUALLY MY FIRST GAME, WHICH I'VE MADE USING ONLY PYTHON (+PYFIGLET) AND I'M STILL WORKING ON IT TO MAKE IT MORE DYNAMIC AND ENTERTAINING :) 


import random
from pyfiglet import Figlet


rd=random.randint(1,100)
score=100

f = Figlet(font='slant')
print(f.renderText('GUESS GAME'))
print("In this game you should guess the number choosen randomly by the computer\n    the more wrong answers you get the less score you will have.\nGOOD LUCK!\n")

def is_EVEN(x):
    if x%2==0:
        return True
    return False


def is_Prime(x):
    for i in range(2,int(x/2)):
        if x%i==0:
            return False
        break
    else:
        return True

while True:
    try:
        numb=int(input("Guess Number Choosen: "))
        if numb==rd:
            print("TRUEEEE!!!\n--> THE CHOOSEN NUMBER IS INDEED:",rd)
            print(f.renderText('YOUR SCORE : '+str(score)))
            print("\n")
            break
        if numb<rd:
            score-=5
            if is_EVEN(rd):
                L=list(int(i) for i in str(rd))
                s=0
                for i in L:
                    s+=i
                if s%2==0:
                    print("EVEN NUMBER + SUM OF ITS DIGITS IS ALSO EVEN")
                else:
                    print("EVEN NUMBER + SUM OF ITS DIGITS IS ODD")
                
            else:
                if is_Prime(rd):
                    print("HINT: IT'S A PRIME NUMBER + BIGGER THAN THE INPUT")
                else:
                    print("BIGGER ODD NUMBER")
        elif numb>rd:
            score-=5
            if is_EVEN(rd):
                print("CHOOSE AN EVEN NUMBER SMALLER THAN PREVIOUS ONE!")
            else:
                if is_Prime(rd):
                    print("HINT: IT'S A PRIME NUMBER + SMALLER THAN THE INPUT")
                else:
                    print("SMALLER ODD NUMBER")
    except ValueError:
        print("YOU SHOULD PRINT A NUMBER")
        break
