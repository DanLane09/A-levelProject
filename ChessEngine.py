# Gets all the legal moves for a pawn on a certain square
def getPawnMoves(playerClicks, colour, board):
    legalMoves = []
    # As black and white pieces require completely different directions to move, it was easier to split the up
    if colour == "b":
        # Increases the row by one for a general legal move
        moveToCheck = playerClicks[0][0] + 1
        goodMove = [moveToCheck, playerClicks[0][1]]
        # Ensures the move is still on the board after being made and the square they are trying to move to is empty
        if -1 < goodMove[1] < 8 and board[goodMove[0]][goodMove[1]] == "--":
            legalMoves.append(goodMove)
        # This lets pawns take to the left, unless they are on the furthest right rank
        if goodMove[1] < 7:
            # Makes sure there is a white piece to take on that square
            if board[goodMove[0]][goodMove[1] + 1] != "--" and board[goodMove[0]][goodMove[1] + 1][0] == "w":
                pawnTake = [goodMove[0], goodMove[1] + 1]
                # Ensures the move stays on the board
                if -1 < pawnTake[1] < 8:
                    legalMoves.append(pawnTake)
        # This lets pawns take to the right, unless they are on the furthest left rank
        if goodMove[1] > 0:
            # Makes sure there is a white piece to take on that square
            if board[goodMove[0]][goodMove[1] - 1] != "--" and board[goodMove[0]][goodMove[1] - 1][0] == "w":
                pawnTake = [goodMove[0], goodMove[1] - 1]
                # Ensures the move stays on the board
                if -1 < pawnTake[1] < 8:
                    legalMoves.append(pawnTake)
        # Allows a double move if the pawn hasn't moved from its starting position
        if playerClicks[0][0] == 1:
            # Increases row by 2
            moveToCheck = playerClicks[0][0] + 2
            goodMove = [moveToCheck, playerClicks[0][1]]
            # Makes sure there is nothing blocking the pawn from making the double move
            if board[goodMove[0]][goodMove[1]] == "--" and board[goodMove[0] - 1][goodMove[1]] == "--":
                legalMoves.append(goodMove)

    # As black and white pieces require completely different directions to move, it was easier to split the up
    if colour == "w":
        # Decreases the row by one for a general legal move
        moveToCheck = playerClicks[0][0] - 1
        goodMove = [moveToCheck, playerClicks[0][1]]
        # Ensures the move is still on the board after being made and the square they are trying to move to is empty
        if -1 < goodMove[1] < 8 and board[goodMove[0]][goodMove[1]] == "--":
            legalMoves.append(goodMove)
        # This lets pawns take to the right, unless they are on the furthest right rank
        if goodMove[1] < 7:
            # Makes sure there is a black piece to take on that square
            if board[goodMove[0]][goodMove[1] + 1] != "--" and board[goodMove[0]][goodMove[1] + 1][0] == "b":
                pawnTake = [goodMove[0], goodMove[1] + 1]
                # Ensures the move stays on the board
                if -1 < pawnTake[1] < 8:
                    legalMoves.append(pawnTake)
        # This lets pawns take to the left, unless they are on the furthest left rank
        if goodMove[1] > 0:
            # Makes sure there is a white piece to take on that square
            if board[goodMove[0]][goodMove[1] - 1] != "--" and board[goodMove[0]][goodMove[1] - 1][0] == "b":
                pawnTake = [goodMove[0], goodMove[1] - 1]
                # Ensures the move stays on the board
                if -1 < pawnTake[1] < 8:
                    legalMoves.append(pawnTake)
        # Allows a double move if the pawn hasn't moved from its starting position
        if playerClicks[0][0] == 6:
            # Decreases row by 2
            moveToCheck = playerClicks[0][0] - 2
            goodMove = [moveToCheck, playerClicks[0][1]]
            # Makes sure there is nothing blocking the pawn from making the double move
            if board[goodMove[0]][goodMove[1]] == "--" and board[goodMove[0] + 1][goodMove[1]] == "--":
                legalMoves.append(goodMove)

    return legalMoves


# Gets all the legal moves for a rook on a certain square
def getRookMoves(playerClicks, board):
    legalMoves = []
    # Keeps track of if the path has been blocked by another piece or not
    blocked = False
    # The piece can be anywhere on the board and still gain all the possible moves
    for i in range(1, 8):
        # Adds the required amount to the column of the first square selected
        moveToCheck = playerClicks[0][1] + i
        goodMove = [playerClicks[0][0], moveToCheck]
        # Ensures the move is still on the board, the piece hasn't been blocked from moving and it is moving to an
        # empty square
        if -1 < goodMove[1] < 8 and blocked == False and board[goodMove[0]][goodMove[1]] == "--":
            legalMoves.append(goodMove)
        # Ensures the move is still on the board, the piece hasn't been blocked from moving and it is moving to a
        # square with a different coloured piece on
        elif -1 < goodMove[1] < 8 and blocked == False \
                and board[goodMove[0]][goodMove[1]][0] != board[playerClicks[0][0]][playerClicks[0][1]][0] \
                and board[goodMove[0]][goodMove[1]] != "--":
            legalMoves.append(goodMove)
            blocked = True
        # Ensures the move is still on the board and it is moving to a square with the same coloured piece on
        elif -1 < goodMove[1] < 8 \
                and board[playerClicks[0][0]][playerClicks[0][1]][0] == board[goodMove[0]][goodMove[1]][0]:
            blocked = True

    # Keeps track of if the path has been blocked by another piece or not
    blocked = False
    # The piece can be anywhere on the board and still gain all the possible moves
    for i in range(1, 8):
        # Subtracts the required amount to the column of the first square selected
        moveToCheck = playerClicks[0][1] - i
        goodMove = [playerClicks[0][0], moveToCheck]
        # Ensures the move is still on the board, the piece hasn't been blocked from moving and it is moving to an
        # empty square
        if -1 < goodMove[1] < 8 and blocked == False and board[goodMove[0]][goodMove[1]] == "--":
            legalMoves.append(goodMove)
        # Ensures the move is still on the board, the piece hasn't been blocked from moving and it is moving to a
        # square with a different coloured piece on
        elif -1 < goodMove[1] < 8 and blocked == False \
                and board[goodMove[0]][goodMove[1]][0] != board[playerClicks[0][0]][playerClicks[0][1]][0] \
                and board[goodMove[0]][goodMove[1]] != "--":
            legalMoves.append(goodMove)
            blocked = True
        # Ensures the move is still on the board and it is moving to a square with the same coloured piece on
        elif -1 < goodMove[1] < 8 \
                and board[playerClicks[0][0]][playerClicks[0][1]][0] == board[goodMove[0]][goodMove[1]][0]:
            blocked = True

    # Keeps track of if the path has been blocked by another piece or not
    blocked = False
    # The piece can be anywhere on the board and still gain all the possible moves
    for i in range(1, 8):
        # Adds the required amount to the row of the first square selected
        moveToCheck = playerClicks[0][0] + i
        goodMove = [moveToCheck, playerClicks[0][1]]
        # Ensures the move is still on the board, the piece hasn't been blocked from moving and it is moving to an
        # empty square
        if -1 < goodMove[0] < 8 and blocked == False and board[goodMove[0]][goodMove[1]] == "--":
            legalMoves.append(goodMove)
        # Ensures the move is still on the board, the piece hasn't been blocked from moving and it is moving to a
        # square with a different coloured piece on
        elif -1 < goodMove[0] < 8 and blocked == False \
                and board[goodMove[0]][goodMove[1]][0] != board[playerClicks[0][0]][playerClicks[0][1]][0] \
                and board[goodMove[0]][goodMove[1]] != "--":
            legalMoves.append(goodMove)
            blocked = True
        # Ensures the move is still on the board and it is moving to a square with the same coloured piece on
        elif -1 < goodMove[0] < 8 \
                and board[playerClicks[0][0]][playerClicks[0][1]][0] == board[goodMove[0]][goodMove[1]][0]:
            blocked = True

    # Keeps track of if the path has been blocked by another piece or not
    blocked = False
    # The piece can be anywhere on the board and still gain all the possible moves
    for i in range(1, 8):
        # Subtracts the required amount to the row of the first square selected
        moveToCheck = playerClicks[0][0] - i
        goodMove = [moveToCheck, playerClicks[0][1]]
        # Ensures the move is still on the board, the piece hasn't been blocked from moving and it is moving to an
        # empty square
        if -1 < goodMove[0] < 8 and blocked == False and board[goodMove[0]][goodMove[1]] == "--":
            legalMoves.append(goodMove)
        # Ensures the move is still on the board, the piece hasn't been blocked from moving and it is moving to a
        # square with a different coloured piece on
        elif -1 < goodMove[0] < 8 and blocked == False \
                and board[goodMove[0]][goodMove[1]][0] != board[playerClicks[0][0]][playerClicks[0][1]][0] \
                and board[goodMove[0]][goodMove[1]] != "--":
            legalMoves.append(goodMove)
            blocked = True
        # Ensures the move is still on the board and it is moving to a square with the same coloured piece on
        elif -1 < goodMove[0] < 8 \
                and board[playerClicks[0][0]][playerClicks[0][1]][0] == board[goodMove[0]][goodMove[1]][0]:
            blocked = True

    return legalMoves


# Gets all the legal moves for a knight on a certain square
def getKnightMoves(playerClicks, board):
    legalMoves = []
    # The nested loop allows all the squares to be reached
    for i in range(-2, 3):
        for j in range(-1, 2):
            moveToCheck1 = playerClicks[0][0] + i
            moveToCheck2 = playerClicks[0][1] + j
            goodMove = [moveToCheck1, moveToCheck2]
            # Conditions to make sure the move is still on the board and to reject any moves calculations that would
            # result in an illegal move
            if -1 < goodMove[0] < 8 and -1 < goodMove[1] < 8 \
                    and j != 0 and i != 0 and i != j and i + 2 != j and j + 2 != i \
                    and board[playerClicks[0][0]][playerClicks[0][1]][0] != board[goodMove[0]][goodMove[1]][0]:
                legalMoves.append(goodMove)

    # The nested loop allows all the squares to be reached
    for i in range(-2, 3):
        for j in range(-1, 2):
            moveToCheck1 = playerClicks[0][0] + j
            moveToCheck2 = playerClicks[0][1] + i
            goodMove = [moveToCheck1, moveToCheck2]
            # Conditions to make sure the move is still on the board and to reject any moves calculations that would
            # result in an illegal move
            if -1 < goodMove[0] < 8 and -1 < goodMove[1] < 8 \
                    and j != 0 and i != 0 and i != j and i + 2 != j and j + 2 != i \
                    and board[playerClicks[0][0]][playerClicks[0][1]][0] != board[goodMove[0]][goodMove[1]][0]:
                legalMoves.append(goodMove)

    return legalMoves


# Gets all the legal moves for a knight on a certain square
def getBishopMoves(playerClicks, board):
    legalMoves = []
    # Keeps track of if the path has been blocked by another piece or not
    blocked = False
    # The piece can be anywhere on the board and still gain all the possible moves
    for i in range(1, 8):
        # Finds all moves from the top left of the board to the bottom right from the piece's current position
        moveToCheck1 = playerClicks[0][0] + i
        moveToCheck2 = playerClicks[0][1] + i
        goodMove = [moveToCheck1, moveToCheck2]
        # Ensures the move is still on the board, the piece hasn't been blocked from moving and it is moving to an
        # empty square
        if -1 < goodMove[0] < 8 and -1 < goodMove[1] < 8 and blocked == False \
                and board[goodMove[0]][goodMove[1]] == "--":
            legalMoves.append(goodMove)
        # Ensures the move is still on the board, the piece hasn't been blocked from moving and it is moving to a
        # square with a different coloured piece on
        elif -1 < goodMove[0] < 8 and -1 < goodMove[1] < 8 and blocked == False \
                and board[goodMove[0]][goodMove[1]][0] != board[playerClicks[0][0]][playerClicks[0][1]][0] \
                and board[goodMove[0]][goodMove[1]] != "--":
            legalMoves.append(goodMove)
            blocked = True
        # Ensures the move is still on the board and it is moving to a square with the same coloured piece on
        elif -1 < goodMove[0] < 8 and -1 < goodMove[1] < 8 \
                and board[playerClicks[0][0]][playerClicks[0][1]][0] == board[goodMove[0]][goodMove[1]][0]:
            blocked = True

    # Keeps track of if the path has been blocked by another piece or not
    blocked = False
    # The piece can be anywhere on the board and still gain all the possible moves
    for i in range(1, 8):
        # Finds all moves from the top right of the board to the bottom left from the piece's current position
        moveToCheck1 = playerClicks[0][0] + i
        moveToCheck2 = playerClicks[0][1] - i
        goodMove = [moveToCheck1, moveToCheck2]
        # Ensures the move is still on the board, the piece hasn't been blocked from moving and it is moving to an
        # empty square
        if -1 < goodMove[0] < 8 and -1 < goodMove[1] < 8 and blocked == False \
                and board[goodMove[0]][goodMove[1]] == "--":
            legalMoves.append(goodMove)
        # Ensures the move is still on the board, the piece hasn't been blocked from moving and it is moving to a
        # square with a different coloured piece on
        elif -1 < goodMove[0] < 8 and -1 < goodMove[1] < 8 and blocked == False \
                and board[goodMove[0]][goodMove[1]][0] != board[playerClicks[0][0]][playerClicks[0][1]][0] \
                and board[goodMove[0]][goodMove[1]] != "--":
            legalMoves.append(goodMove)
            blocked = True
        # Ensures the move is still on the board and it is moving to a square with the same coloured piece on
        elif -1 < goodMove[0] < 8 and -1 < goodMove[1] < 8 \
                and board[playerClicks[0][0]][playerClicks[0][1]][0] == board[goodMove[0]][goodMove[1]][0]:
            blocked = True

    # Keeps track of if the path has been blocked by another piece or not
    blocked = False
    # The piece can be anywhere on the board and still gain all the possible moves
    for i in range(1, 8):
        # Finds all moves from the bottom left of the board to the top right from the piece's current position
        moveToCheck1 = playerClicks[0][0] - i
        moveToCheck2 = playerClicks[0][1] + i
        goodMove = [moveToCheck1, moveToCheck2]
        # Ensures the move is still on the board, the piece hasn't been blocked from moving and it is moving to an
        # empty square
        if -1 < goodMove[0] < 8 and -1 < goodMove[1] < 8 and blocked == False \
                and board[goodMove[0]][goodMove[1]] == "--":
            legalMoves.append(goodMove)
        # Ensures the move is still on the board, the piece hasn't been blocked from moving and it is moving to a
        # square with a different coloured piece on
        elif -1 < goodMove[0] < 8 and -1 < goodMove[1] < 8 and blocked == False \
                and board[goodMove[0]][goodMove[1]][0] != board[playerClicks[0][0]][playerClicks[0][1]][0] \
                and board[goodMove[0]][goodMove[1]] != "--":
            legalMoves.append(goodMove)
            blocked = True
        # Ensures the move is still on the board and it is moving to a square with the same coloured piece on
        elif -1 < goodMove[0] < 8 and -1 < goodMove[1] < 8 and \
                board[playerClicks[0][0]][playerClicks[0][1]][0] == board[goodMove[0]][goodMove[1]][0]:
            blocked = True

    # Keeps track of if the path has been blocked by another piece or not
    blocked = False
    # The piece can be anywhere on the board and still gain all the possible moves
    for i in range(1, 8):
        # Finds all moves from the bottom right of the board to the top left from the piece's current position
        moveToCheck1 = playerClicks[0][0] - i
        moveToCheck2 = playerClicks[0][1] - i
        goodMove = [moveToCheck1, moveToCheck2]
        # Ensures the move is still on the board, the piece hasn't been blocked from moving and it is moving to an
        # empty square
        if -1 < goodMove[0] < 8 and -1 < goodMove[1] < 8 and blocked == False \
                and board[goodMove[0]][goodMove[1]] == "--":
            legalMoves.append(goodMove)
        # Ensures the move is still on the board, the piece hasn't been blocked from moving and it is moving to a
        # square with a different coloured piece on
        elif -1 < goodMove[0] < 8 and -1 < goodMove[1] < 8 and blocked == False \
                and board[goodMove[0]][goodMove[1]][0] != board[playerClicks[0][0]][playerClicks[0][1]][0] \
                and board[goodMove[0]][goodMove[1]] != "--":
            legalMoves.append(goodMove)
            blocked = True
        # Ensures the move is still on the board and it is moving to a square with the same coloured piece on
        elif -1 < goodMove[0] < 8 and -1 < goodMove[1] < 8 and \
                board[playerClicks[0][0]][playerClicks[0][1]][0] == board[goodMove[0]][goodMove[1]][0]:
            blocked = True

    return legalMoves


# Gets all the legal moves for a queen on a certain square
def getQueenMoves(playerClicks, board):
    legalMoves = []
    # As the queen makes the same moves as the rook and bishop, reuse those functions to get a list of legal moves
    moreMoves1 = getRookMoves(playerClicks, board)
    moreMoves2 = getBishopMoves(playerClicks, board)
    # Adds each move to the array one at a time so it can be easily searched later
    for i in range(0, len(moreMoves1)):
        legalMoves.append(moreMoves1[i])
    for i in range(0, len(moreMoves2)):
        legalMoves.append(moreMoves2[i])

    return legalMoves


# Gets all the legal moves for a queen on a certain square
def getKingMoves(playerClicks, board):
    legalMoves = []
    # The nested loop allows every square around the king to be reached
    for i in range(-1, 2):
        for j in range(-1, 2):
            # Adds the required number to the king's current square to get the move
            moveToCheck1 = playerClicks[0][0] + i
            moveToCheck2 = playerClicks[0][1] + j
            goodMove = [moveToCheck1, moveToCheck2]
            # Ensures the move is still on the board and the square doesn't have a piece of the same colour already
            # on it
            if -1 < goodMove[0] < 8 and -1 < goodMove[1] < 8 \
                    and board[playerClicks[0][0]][playerClicks[0][1]][0] != board[goodMove[0]][goodMove[1]][0]:
                legalMoves.append(goodMove)

    return legalMoves


class GameState:
    def __init__(self):
        # Represents the board in a 2D array to visualise what is happening during the game
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
        ]

        # Keeps track of who's move it is
        self.whiteToMove = True
        # Keeps track of all the moves made in a game
        self.moveLog = []

    # Makes the move by changing the elements in the array representation of the board
    def makeMove(self, move):
        self.board[move.firstRow][move.firstCol] = "--"
        self.board[move.secondRow][move.secondCol] = move.pieceMoved
        self.moveLog.append(move)
        # Changes who's turn it is to make a move
        self.whiteToMove = not self.whiteToMove

    # Reverses the last move made by changing the elements in the array representation of the board
    def undoMove(self):
        move = self.moveLog.pop()
        self.board[move.firstRow][move.firstCol] = move.pieceMoved
        self.board[move.secondRow][move.secondCol] = move.pieceCaptured
        # Changes who's turn it is to make a move
        self.whiteToMove = not self.whiteToMove

    # Finds what piece is on the selected square and finds the correct function to find the legal moves for that
    # piece in that position
    def possibleMoves(self, playerClicks):
        validMoves = []
        row = playerClicks[0][0]
        col = playerClicks[0][1]
        colour = self.board[row][col][0]
        piece = self.board[row][col][1]
        # Checks that the colour of the selected piece matches with who's turn it is
        if colour == "w" and self.whiteToMove == True or colour == "b" and self.whiteToMove == False:
            if piece == "P":
                validMoves = getPawnMoves(playerClicks, colour, self.board)
            if piece == "R":
                validMoves = getRookMoves(playerClicks, self.board, )
            if piece == "N":
                validMoves = getKnightMoves(playerClicks, self.board)
            if piece == "B":
                validMoves = getBishopMoves(playerClicks, self.board)
            if piece == "Q":
                validMoves = getQueenMoves(playerClicks, self.board)
            if piece == "K":
                validMoves = getKingMoves(playerClicks, self.board)
        # If the wrong person tries to move, they are told by the program
        else:
            print("Wait for your turn!")
        print(validMoves)
        return validMoves


class Move:
    # Holds the ranks and files in the corresponding index values of the board representation
    ranks = [8, 7, 6, 5, 4, 3, 2, 1]
    files = ["a", "b", "c", "d", "e", "f", "g", "h"]

    # Sets the variables that can be used more easily than index values
    def __init__(self, firstSq, secondSq, board):
        self.firstRow = firstSq[0]
        self.firstCol = firstSq[1]
        self.secondRow = secondSq[0]
        self.secondCol = secondSq[1]
        self.pieceMoved = board[self.firstRow][self.firstCol]
        self.pieceCaptured = board[self.secondRow][self.secondCol]

    # Shows the user the move that was made in basic chess notation
    def ChessNotation(self):
        print(self.getRankFile(self.firstRow, self.firstCol), "moved to ", self.getRankFile(self.secondRow, self.
                                                                                            secondCol))

    # Converts the index values into ranks and files so it makes more sense to the user
    def getRankFile(self, r, c):
        return self.files[c], self.ranks[r]
