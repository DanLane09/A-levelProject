# Imports all the libraries and other files I will use for this program
import random
import pygame
from Chess import ChessEngine

# Sets global constants used throughout the program to help with the visuals of the program
WIDTH = HEIGHT = 560
SQUARES = 8
SIZE = HEIGHT // SQUARES
ICONS = {}


# Loads all the pictures for the pieces into a list so they can easily be accessed at any point throughout the program
def loadImages():
    pieces = ["wK", "wQ", "wB", "wR", "wN", "wP", "bK", "bQ", "bB", "bR", "bN", "bP"]
    for piece in pieces:
        ICONS[piece] = pygame.transform.scale(pygame.image.load("images/" + piece + ".png"), (SIZE, SIZE))


# All the main logic for what happens when in the program is done in  this function
def main():
    # Sets the pygame window up to allow for the squares and pieces to be drawn on
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    window.fill(pygame.Color("white"))
    # Importing a class from the other file so it can be referenced easily and its variables can be used in this file
    gameState = ChessEngine.GameState()
    # Sets the pygame window to run continuously
    run = True
    # Opens and formats the external file for later in the program when the move long saved to the external file
    f = open("Move Log.txt", "a")
    f.write("\n\n")
    # Calls the function to save all the piece images in the list
    loadImages()
    # These variables are used throughout to hold the index values of the squares that the user clicks on to move pieces
    sqSelected = ()
    playerClicks = []
    # Contains the index values of all the black pieces so the computer is aware of where the pieces are so it can
    # move them when playing against the user
    blackSquares = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7],
                    [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7]]
    # The following is run until the user quits the pygame window
    while run:
        for event in pygame.event.get():
            # Looks for the user quitting the pygame window
            if event.type == pygame.QUIT:
                # Appends the moveLog to the external file
                f.write(str(gameState.moveLog))
                f.close()
                # Stops the pygame window showing and ends the program
                run = False
            # Looks for a click from the user's mouse and makes sure it is white's turn to make a move
            elif event.type == pygame.MOUSEBUTTONDOWN and gameState.whiteToMove == True:
                # Gets the coordinates of where the user clicked on the screen
                coordinates = pygame.mouse.get_pos()
                # Converts these coordinates into the index values used in the board array representation
                col = coordinates[0] // SIZE
                row = coordinates[1] // SIZE
                # Stops the user selecting an empty square to move around the board
                if sqSelected == [row, col] or (gameState.board[row][col] == "--" and len(playerClicks) == 0):
                    sqSelected = ()
                    playerClicks = []
                # Takes the index value of where the user clicked on the screen and saves it in a variable to be
                # referenced when making the move
                else:
                    sqSelected = [row, col]
                    playerClicks.append(sqSelected)
                # This section will only run if the user has selected 2 squares: one to move from and one to move to
                if len(playerClicks) == 2:
                    # Converts the squares that the user has selected into a readable format for the program
                    move = ChessEngine.Move(playerClicks[0], playerClicks[1], gameState.board)
                    # Finds all the legal moves for the piece in the first square the user selected
                    legalMoves = gameState.possibleMoves(playerClicks)
                    wantedMove = [row, col]
                    # Removes the captured piece from the list containing the position of all the black pieces to
                    # speed up the computer in the endgame when less pieces are on the board
                    if gameState.board[playerClicks[1][0]][playerClicks[1][1]][0] == "b":
                        i = 0
                        while i < len(blackSquares):
                            if blackSquares[i] == playerClicks[1]:
                                blackSquares.pop(i)
                            i = i + 1
                    # If the move that the user wants to make is legal then it is outputted to the user and then the
                    # move is made in the program
                    if wantedMove in legalMoves:
                        print(move.ChessNotation())
                        gameState.makeMove(move)
                    # Tells the user if the move they want to make is not legal
                    elif legalMoves:
                        print("Not a legal move")
                    # Sets the variables to empty so the next iteration of the code will happen correctly and
                    # efficiently
                    sqSelected = ()
                    playerClicks = []
            # Lets the computer make its move for black
            elif not gameState.whiteToMove:
                # Makes sure there are still pieces the computer can move, if there aren't then black has lost
                if len(blackSquares) != 0:
                    # Chooses a random piece to move and finds all the legal moves for that piece in that position
                    pieceToMove = random.randint(0, len(blackSquares) - 1)
                    playerClicks.append(blackSquares[pieceToMove])
                    legalMoves = gameState.possibleMoves(playerClicks)
                    # Ensures there are legal moves for that piece in that position
                    if len(legalMoves) != 0:
                        # Finds a random square in the list of legal moves that the piece can move to
                        squareMoveTo = random.randint(0, len(legalMoves) - 1)
                        moveToMake = legalMoves[squareMoveTo]
                        # Converts the squares that the user has selected into a readable format for the program
                        move = ChessEngine.Move(playerClicks[0], moveToMake, gameState.board)
                        print(move.ChessNotation())
                        # The move is made on the board representation
                        gameState.makeMove(move)
                        # Changes where the piece is so the computer remembers for the next move
                        blackSquares[pieceToMove] = legalMoves[squareMoveTo]
                # If there are no more black pieces, then the game is over
                else:
                    print("I have been defeated")
                sqSelected = []
                playerClicks = []
            # This is the undo function that allows the user to go back a move if they have made a mistake
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    gameState.undoMove()
                    sqSelected = []
                    playerClicks = []
        # Updates the game window so it can be seen accurately by the user
        drawGameState(window, gameState)
        clock.tick()
        pygame.display.flip()


# Calls other functions to draw the board and the pieces
def drawGameState(window, gameState):
    drawBoard(window)
    drawPieces(window, gameState.board)


# Draws squares of the correct colour in the correct places on the board
def drawBoard(window):
    colours = [pygame.Color("white"), pygame.Color("dark grey")]
    for row in range(SQUARES):
        for col in range(SQUARES):
            # Finds which colour the square should be by finding the remainder after the MOD 2 operation
            colour = colours[((row + col) % 2)]
            pygame.draw.rect(window, colour, pygame.Rect(col * SIZE, row * SIZE, SIZE, SIZE))


# Draws pieces of the correct colour in the correct places on the board
def drawPieces(window, board):
    for row in range(SQUARES):
        for col in range(SQUARES):
            piece = board[row][col]
            if piece != "--":
                window.blit(ICONS[piece], (col * SIZE, row * SIZE))


# Calls the main function to begin the program
if __name__ == "__main__":
    main()
