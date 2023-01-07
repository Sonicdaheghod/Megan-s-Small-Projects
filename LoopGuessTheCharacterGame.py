#Here, I am practicing how to loop a game

import random

while True:
    print("-----------Guess What I'm Thinking!-----------\n")
    print("Please enter the character I am thinking of... _________ the Hedgehog?\n")
    mySide =random.choice(["Sonic","Shadow","Silver"])
    playerAnswer = input("Sonic, Shadow, Or Silver?\n")
    if str(playerAnswer) in ["Sonic","Shadow","Silver"]:
        if str(playerAnswer) == mySide:
            print("That's right!")
        else:
            print("That is incorrect.")
    else:
            print("That's not what I asked for, loser.")

        #The looping

    askPlayAgain = input("Press Y to play again. Otherwise, hit any key to exit.")
    if askPlayAgain == "Y":
        continue
    else: 
        break
        

        
