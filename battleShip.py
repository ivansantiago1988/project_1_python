""" Complete your "Project Details".  If there is an arrow to the right of the line number then click the arrow
to expand the comment.
********************************************************
COMP 1005/1405 Section [E] - Assignment [3]

Project Details:
    Name: Ivan Guevara
    Student #: 100754875
    Date Created: [2024-11-03]

External Libraries Used (if appliable)
********************************************************
"""
""" Pseudocode 
        Prompt user input for total rounds of the game
        Initialize the total game score
        for each round:
            Validate the user input for board size and number of ships
            Handle invalid entries 
            Set the board and ships.
            for each shot in the round:
                Request the user to input the assumed ship coordinates
                Display the Hit message (Hit or Miss)
                Display the full board with updated attempts results 
            Show the final state of the board
            Display the user final score of this round
        Display the user final score of the game
"""

""" Import the libraries if appliable

"""
import random

""" Define global variables if appliable

"""
totalScore = 0

# Suggest to start by understanding the code in the main function.
# Then proceed with the coding.


def addShip(board, numShips):
    """ Function Description:
            Randomly places the specified number of ships ('S') on the board.
        Parameter(s): 
            board : The list of lists representing the game board
            numShips [int]: The number of ships that user wants on the board
        Return: None   
    """

    size = len(board)
    pairs = [(row, col) for row in range(size) for col in range(size)]
    random.shuffle(pairs)   
    selected_positions = pairs[:numShips]           
    for k in range(numShips):
        board[selected_positions[k][0]][selected_positions[k][1]] = "S"


    return board

def checkSetUpError(size, numShips):
    """ Function Description:
            Validates user input for the size of the board and the number of ships.
        Parameter(s): 
            size [int]: The size of the board
            numShips [int]: The number of ships
        Return [Boolean]: Return True if an error is found or False if there is no error.
    """
    output = False
    if(size >= 2 and size <= 5 and numShips >= 1 and numShips <= ((size*size) -2)):
        output = False
    else:
        output = True
        
    return output

def checkFireError(board, row, col):
    """ Function Description:
            Validates user input for the coordinates to shot a ship
        Parameter(s):
            board : The list of lists representing the game board
            row [int]: The row coordinate entered by the user.
            col [int]: The col coordinate entered by the user. 
        Return [Boolean]: Return True if an error is found or False if there is no error.   
    """
    size = len(board)
    err = False
    if(row >= 0 and row < size and col >= 0 and col < size):
        if(board[row][col] == "X" or board[row][col] == "O"):
            print("Already fired at that locaton. Enter new coordinates")
            err = True
        else:
            err = False
    else:
        print("You will need to enter valid coordinates")
        err = True
        
    return err

def createBoard(size):
    """ Function Description:
            Creates a size-by-size game board initialized with '~'
        Parameter(s):
            size [int]: The size of the board which will be used to create a board of size x size
                        Example: size 2 will create [ ['~', '~'], ['~', '~']]
        Return: board which is a list of lists  
    """
    list_double = []
    for row in range(size):
        list_data = []
        for column in range(size):
            list_data.append("~")
        list_double.append(list_data)
    
    return list_double

def displayBoard(board, round=True):
    """ Function Description:
            Displays the current state of the board.  If round is True then print out the current
            state of the board without showing the ships 'S'.  Else round is False then print out the
            current state of the board showing hits 'X', misses 'O', ships that have not been hit 'S'
            and everything else '~'.
        Parameter(s):
            board : The list of lists representing the game board.
            round [Boolean] : True if you are print the board after each shot and False to display
            the end of a round version.  Default value of True.
        
        Return: None  
    """

    if(round == True):
     for i in range(len(board)):
          for j in range(len(board)):
               if(board[i][j] == "S"):
                    print("~", end=" ")
               else:
                    print(board[i][j], end=" ")
          print("")
    else:
     for i in range(len(board)):
          for j in range(len(board)):
               print(board[i][j], end=" ")
          print("")

    return None

def fireShot(board, row, col):
    """ Function Description:
            Marks a shot on the board.
        Parameter(s):
            board : The list of lists representing the game board
            row [int]: The row coordinate entered by the user.
            col [int]: The col coordinate entered by the user. 
        Return[Boolean]: Return True if a ship was hit and False if the shot missed a ship.     
    """  
    
    hit = False
    value = board[row][col]
    if(value == "S"):
        board[row][col] = "X" 
        hit = True
    else:
        board[row][col] = "O"
        hit = False

    return hit

def playRound(board, numShips):
    """ Function Description:
            Main logic for playing one round 
            
            Pseudocode:
            Keep track of number of shots for the round
            Keep track of the score (number of hits) for the round
            Loop until user fires all their shots
                Ask user to enter coordinates for their shot.  Input two numbers separated by a space.
                Validate the shot coordinates using checkFireError function
                Fire a shot using the fireShot function
                Output if the shot is a hit or a miss
                display the board after the shot has been taken displayBoard(board)
            Output "End of round X"
            display the board at the end of the round displayBoard(board, False)
    
        Parameter(s):
            board : The list of lists representing the game board
            numShips [int]: The number of ships
        Return [int]: The number of hits (ships that were hit) for the round.   
    """

    shots = 1
    shots_hit = 0
    while(shots < numShips+1):
        row, col = input("Enter row and column to take a shot (e.g 2 3):").split()
        err = checkFireError(board,int(row),int(col))

        while(err):
            row, col = input("Enter row and column to take a shot (e.g 2 3):").split()
            err = checkFireError(board,int(row),int(col))
    
    
        hit =  fireShot(board,int(row),int(col))
        if(hit == True):
            shots_hit = shots_hit + 1
            print(f"Shot {shots} is a Hit!")
        else:
            print(f"Shot {shots} is a Miss!")


        displayBoard(board)
        shots = shots + 1

    print("End of round: ")   
    displayBoard(board, False)
    print("The number of ships shot", shots_hit)

    return shots_hit

def main():    
    """ Function Description:
            Play the game in a designated number of rounds and present the final score to the user.
            You can not change the code in the main function.  If student changes the main function code
            then they will lose 25 marks.
        Parameter(s): No parameters
        Return: None  
    """
    currentRound = 0
    numRounds = int(input("Enter the number of rounds of Battleship you want to play: "))
    flag = True
    while currentRound < numRounds:
        while flag:
            size = int(input("Enter the size of the board: "))
            numShips = int(input("Enter the number of ships: "))
            flag = checkSetUpError(size, numShips)
            if (flag == False):
                break
            else:
                print("You will need to enter the size of the board and number of ships again.")
            
        board = createBoard(size)
        addShip(board, numShips)
        print(f"\nRound {currentRound + 1}:\n")
        hits = playRound(board, numShips)
        global totalScore
        totalScore += hits
        currentRound += 1
    print(f"\nFinal Score after {numRounds} round(s) is {totalScore} out {numShips * numRounds}.")
    return

if __name__ == '__main__':
    main()
