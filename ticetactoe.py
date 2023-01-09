#creating board
gameBoard = ["_","_","_",
            "_","_","_",
            "_","_","_",]

#defining format of the board 3x3
def displaygameBoard():
    print("|" + gameBoard[0] + "|" + gameBoard[1]+ "|" + gameBoard[2] + "|")
    print("|" + gameBoard[3] + "|" + gameBoard[4]+ "|" + gameBoard[5] + "|")
    print("|" + gameBoard[6] + "|" + gameBoard[7]+ "|" + gameBoard[8] + "|")

#defining the function for the game aspect
def beginGame():

#have terminal bring up the board we made and the function where user places thier piece
    displaygameBoard()

    whoseTurn()

#having user tell us where they want to put their piece on board
def whoseTurn():
    placeBoard = input("Choose a position from 0-8\n")
    placeBoard = int(placeBoard) 
            
#getting something to be placed on board based on user input
    gameBoard[placeBoard] = "X"
    displaygameBoard()

#run program to bring up the board game and its function
beginGame()
