#creating board
gameBoard = ["_","_","_",
            "_","_","_",
            "_","_","_",]

#seeing that the game itself is still going
gameRunning = True

#Who is winner? Is there a tie?
isWinner = None

#Whos turn is it right now
currentUser = "X"

#defining format of the board 3x3
def displaygameBoard():
    print("|" + gameBoard[0] + "|" + gameBoard[1]+ "|" + gameBoard[2] + "|")
    print("|" + gameBoard[3] + "|" + gameBoard[4]+ "|" + gameBoard[5] + "|")
    print("|" + gameBoard[6] + "|" + gameBoard[7]+ "|" + gameBoard[8] + "|")

#defining the function for the game aspect
def beginGame():

#have terminal bring up the board we made
    displaygameBoard()

 while gameRunning: 
#these three functions below are what the terminal will follow while running the game of tic tac toe (after person makes a move, it sees if the game should end, if not then the other user makes a move,then its goes through the process again)
    theTurn(currentUser)

    isGameOver()

    otherPlayerTurn()

#having user tell us where they want to put their piece on board
def theTurn():
    placeBoard = input("Choose a position from 0-8\n")
    placeBoard = int(placeBoard) 
#getting something to be placed on board based on user input
    gameBoard[placeBoard] = "X"
    displaygameBoard()

#bringing the "isGameOver" fucntion to work
def isGameOver():
    isWinner()
    bothTie()

#defining the winner function
def isWinner():
    return
#defining the tie function
def bothTie():
    return

#Time to define function to change whose turn it is
def otherPlayerTurn():
    return
#run program to bring up the board game and its function
beginGame()

#23:21 https://www.youtube.com/watch?v=BHh654_7Cmw

