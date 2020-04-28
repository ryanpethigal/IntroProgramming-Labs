symbol = [" ", "x", "o"]


def printRow(row):
    # initialize output to the left border
    print("|", end=" ")
    # for each square in the row
    for x in range(len(row)):
        # output the symbol for this square followed by a border
        print("%2s|" % (symbol[row[x]] + " "), end=" ")


def printBoard(board):
    # print the top border
    print('')
    print(('+---' * 3) + '+')
    # for each row in board
    for i in range(len(board)):
        printRow(board[i])  # print the row
        # print the next border
        print('\n' + '+---' * 3 + '+')


def markBoard(board, row, col, player):
    if (row >= 0):
        if row < len(board):
            if col >= 0:
                if col < len(board) :
                    if board[row][col] == 0:
                        board[row][col] = player # Set to player number
                        return True
    else:
        return False


def getPlayerMove():
    # prompt the user for row and column separately
    row = int(input("Enter row number 1, 2, or 3: "))
    column = int(input("Enter column number 1, 2, or 3: "))

    return (row-1, column-1)  # return the row and column as a tuple


def hasBlanks(board):
    for x in range(len(board)):
        for i in range(len(board[x])):
            if (board[x][i] == 0):
                return True
    else:
        return False


def main():
    board = [[0 for x in range(3)] for i in range(3)] # 0's to start
    player = 1
    while hasBlanks(board):
        printBoard(board)
        row, col = getPlayerMove()
        while (not markBoard(board, row, col, player)):
            row, col = getPlayerMove()
        player = player % 2 + 1  # switch player for next turn


main()