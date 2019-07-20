#!/usr/bin/python

# Head ends here

def next_move(posr, posc, board):
    if board[posr][posc] == 'd':
        print("CLEAN")
        return

    num_r = len(board)
    num_c = len(board[0])
    
    # get locations of all dirty cells
    locs = []
    dists = []
    for r in range(num_r):
        for c in range(num_c):
            if board[r][c] == 'd':
                locs.append((r, c))
                dist = abs(posr-r) + abs(posc-c)
                dists.append(dist)

    # get min distance to get nearest dirty cell
    min_index = dists.index(min(dists))
    nearest_d = locs[min_index]

    # get min dimension
    y_dist = nearest_d[0] - posr
    x_dist = nearest_d[1] - posc

    if (x_dist == 0) or ((abs(y_dist) < abs(x_dist)) and (y_dist > 0)):
        if y_dist < 0:
            print("UP")
        else:
            print("DOWN")

    else:
        if x_dist < 0:
            print("LEFT")
        else:
            print("RIGHT")

    return
    
# Tail starts here

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)