#The variables inside the two dotted lines are global variables
#------------------------------------------
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
#------------------------------------------

#defining format of the board 3x3
def displaygameBoard():
    print("|" + gameBoard[0] + "|" + gameBoard[1]+ "|" + gameBoard[2] + "|")
    print("|" + gameBoard[3] + "|" + gameBoard[4]+ "|" + gameBoard[5] + "|")
    print("|" + gameBoard[6] + "|" + gameBoard[7]+ "|" + gameBoard[8] + "|")

#starts game of tic tac toe
def beginGame():

#have terminal bring up the board we made
    displaygameBoard()

    while gameRunning: 
#these three functions below are what the terminal will follow while running the game of tic tac toe (after person makes a move, it sees if the game should end, if not then the other user makes a move,then its goes through the process again)
    #deals with the current turn of a player
        theTurn(currentUser)
    #sees if the game ends
        isGameOver()
    #moves to other player for their turn to place piece on board
        otherPlayerTurn()
    #game ends (if there is a winner or if it leads to tie)
    if isWinner == "X" or isWinner == "0":
        print(isWinner + "wins the game! Congrats!")
    elif isWinner == None:
        print("It's a tie!")
#having user tell us where they want to put their piece on board
def theTurn(player):
    #you can insert player since def theTurn requires one argument (one thing)
    placeBoard = input("Choose a position from 0-8\n")
    placeBoard = int(placeBoard) 


#getting something to be placed on board based on user input
    gameBoard[placeBoard] = "X"
    displaygameBoard()

#bringing the "isGameOver" function to work
def isGameOver():
    isWinner()
    bothTie()

#defining the winner function
def isWinner():
    
    #declaring global variables that we want to bring
    global isWinner
    #see if win is in a row
    threeInRow = checkRows()
    #column
    threeInColumn = checkColumns()
    #diagonal
    threeInDiagonal = checkDiagonals()
#defining how to handle conditions that means one wins/loses the game
    if threeInRow:
        #they win
        isWinner = threeInRow()
    elif threeInColumn:
        #they win
        isWinner = threeInColumn()
    elif threeInDiagonal:
        #they win
        isWinner = threeInDiagonal()
    else:
        #they lose
        isWinner = None
#looks to see if there is three in a row
def checkRows():
    return
#looks to see if there is three in a column
def checkColumns():
    return
#looks to see if there is three in a diagonal
def checkDiagonals():
    return

#defining the tie function
def bothTie():
    return

#Time to define function to change whose turn it is
def otherPlayerTurn():
    return
#run program to bring up the board game and its function
beginGame()

#35:43 https://www.youtube.com/watch?v=BHh654_7Cmw
