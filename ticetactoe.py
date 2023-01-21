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

#define format of template board to show what each number represents
def displayTemplateBoard():
    print("|" + "0" + "|" + "1"+ "|" + "2" + "|")
    print("|" + "3" + "|" + "4" + "|" + "5" + "|")
    print("|" + "6" + "|" + "7" + "|" + "8" + "|")
#starts game of tic tac toe
def beginGame():

#have terminal bring up the two board we made
    print("----------Game of Tic Tac Toe!----------")
    displaygameBoard()
    displayTemplateBoard()

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
        print (isWinner + " wins the game! Congrats!")
    elif isWinner == None:
        print("It's a tie!")
#having user tell us where they want to put their piece on board
def theTurn(player):

    #shows whose turn it is
    print(player + "'s turn")
    #you can insert player since def theTurn requires one argument (one thing)
    placeBoard = input("Choose a position from 0-8:\n")

    valid = False
    while not valid:
    #while loop allows program to keep checking if input is in or out of range for gameboard position
        while placeBoard not in ["0", "1","2","3","4","5","6","7","8"]:
            placeBoard = input("That's not a valid input. Choose a position from 0-8:\n")
        
        placeBoard = int(placeBoard)

        if gameBoard[placeBoard] == "_":
            valid = True
        else:
            print("This spot is already taken. Chooose another spot.")
#getting something to be placed on board based on user input

#make sure this is indented to show it is part of  "theTurn" function
    gameBoard[placeBoard] = player
    displaygameBoard()
    displayTemplateBoard()

#bringing the "isGameOver" function to work
def isGameOver():
    seeIfWinner()
    bothTie()

#defining the winner function
def seeIfWinner():
    
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
        ### remember () are only for functions
        #they win
        isWinner = threeInRow
    elif threeInColumn:
        #they win
        isWinner = threeInColumn
    elif threeInDiagonal:
        #they win
        isWinner = threeInDiagonal
    else:
        #they lose
        isWinner = None
    return
#looks to see if there is three in a row
def checkRows():
    global gameRunning
    #if top row is a win -- check for each of the three rows we have 
    firstRow = gameBoard[0] == gameBoard[1] == gameBoard[2] != "_"
    secondRow = gameBoard[3] == gameBoard[4] == gameBoard[5] != "_"
    thirdRow = gameBoard[6] == gameBoard[7] == gameBoard[8] != "_"
    #if statement - lets program know game is no longer going since we reached a winner
    if firstRow or secondRow or thirdRow:
        gameRunning = False
    #showing player where the row win occured
    if firstRow:
        return gameBoard[0]
    elif secondRow:
        return gameBoard[3]
    elif thirdRow:
        return gameBoard[6]
    return
#looks to see if there is three in a column
def checkColumns():
    global gameRunning

    firstColumn = gameBoard[0] == gameBoard[3] == gameBoard[6] != "_"
    secondColumn = gameBoard[1] == gameBoard[4] == gameBoard[7] != "_"
    thirdColumn = gameBoard[2] == gameBoard[5] == gameBoard[8] != "_"
    #the if statement
    if firstColumn or secondColumn or thirdColumn:
        gameRunning = False
    if firstColumn:
        return gameBoard[0]
    elif secondColumn:
        return gameBoard[1]
    elif thirdColumn:
        return gameBoard[2]
    return
#looks to see if there is three in a diagonal
def checkDiagonals():
#bring in global variables
    global gameRunning
#only two diagonals can be a win
    diagonal1 = gameBoard[6] == gameBoard[4] == gameBoard[2] != "_"
    diagonal2 = gameBoard[0] == gameBoard[4] == gameBoard[8] != "_"
    #if statement
    if diagonal1 or diagonal2:
        gameRunning = False

    if diagonal1:
        return gameBoard[6]
    elif diagonal2:
        return gameBoard[0]
    return

#defining the tie function
def bothTie():
#global variables
    global gameRunning
    #if there are no spots avaliable on the board we made
    if "_" not in gameBoard:
        gameRunning = False
    return

#Time to define function to change whose turn it is
def otherPlayerTurn():
    #must bring in global variables
    global currentUser

    if currentUser == "X":
        currentUser = "O"
    elif currentUser == "O":
        currentUser = "X"

    return
#run program to bring up the board game and its function
beginGame()

#Link used for game template: https://www.youtube.com/watch?v=BHh654_7Cmw
