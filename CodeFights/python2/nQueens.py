def printBoard(board, n):
    print "------------------"
    for row in xrange(0,n):
        for col in xrange(0,n):
            print board[row][col],
        print "\n",

def isValidPosition(board, n, row, col):
    # check row
    for i in xrange(0,n):
        if board[row][i] == 1: return False
    # check column
    for i in xrange(0,n):
        if board[i][col] == 1: return False
    # check diagonal
    i = row
    j = col
    i_diff = 1
    j_diff = 1
    while True:
        if board[i][j] == 1:
            return False

        i += i_diff
        j += j_diff

        if i == n or j == n:
            i = row
            j = col
            i_diff *= -1
            j_diff *= -1

        if i < 0 or j < 0:
            i = row
            j = col
            break

    i_diff = 1
    while True:
        if board[i][j] == 1:
            return False

        i += i_diff
        j += j_diff

        if i == n or j < 0:
            i = row
            j = col
            i_diff *= -1
            j_diff *= -1

        if i < 0 or j == n:
            break

    return True

def placeQueenInColumn(board, n, col, row_list, start_row, isStart, row_array):
    end = n
    if isStart:
        end = start_row + 1
    for row in xrange(start_row, end):
        if isValidPosition(board, n, row, col):
            board[row][col] = 1
            row_list.append(row + 1)
            col += 1
            #printBoard(board, n)
            if col == n:
                temp = list(row_list)
                row_array.append(temp)
                col -= 1
                row_list.pop()
                board[row][col] = 0
                continue

            n_row = placeQueenInColumn(board, n, col, row_list, 0, False, row_array)
            if n_row != -1:
                return row
            col -= 1
            row_list.pop()
            board[row][col] = 0
    
    return -1
'''
def placeQueens(board, n, row_list):
    col = 0
    while col < n:
        row = 0
        while row < n:
            if isValidPosition(board, n, row, col):
                board[row][col] = 1
                row_list.append(row + 1)
                col += 1
                if col == n:
                    #return row
                # move deeper into stack
                
                if n_row != -1:
                    #return row
                row_list.pop()

    return -1
'''
def nQueens(n):
    row_array = []
    for row_start in xrange(0,n):
        row_list = []
        board = [[0 for i in xrange(0,n)] for i in xrange(0,n)]
        col = 0
        if placeQueenInColumn(board, n, col, row_list, row_start, True, row_array) != -1:
            pass
        
    return row_array

print nQueens(5)
