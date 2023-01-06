#game template credit to freecodecamp.org
#https://www.youtube.com/watch?v=8ext9G7xspg&t=1274s

import random

#starting the function
def play():
    print("-------Ultimate Rock, Paper, Scissors Game!--------\n")
    user = input("What's your choice? 'r' for rock, 'p' for paper', or 's' for scissors?\n")
    #asks user what choice they want and is for the user to type their choice
    computer = random.choice(['r','p','s'])
    #computer randomly chooses from the list

    if user == computer:
        return("It's a tie!")
#defining what happens if you win, other wise you lose condition
    if is_win(user,computer):
        return 'You won!'

    return("You lost!")
#setting each condition for win in the game
def is_win(player,opponent):
    if(player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True

#keep game going, set play again variable (working on now)

print(play())
#need this to start the game 
