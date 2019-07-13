#!/usr/bin/python

# Head ends here

def next_move(posr, posc, board):
    if board[posr][posc] == 'd':
        print("CLEAN")
        return
    
    num_r = len(board)
    num_c = len(board[0])
    
    # check row for dirty cells
    cur_row_ds = [c for c in range(num_c) if board[posr][c] == 'd']
    if len(cur_row_ds) > 0:
        dists = [c - posc for c in cur_row_ds]
        min_index = dists.index(min(dists))
        if cur_row_ds[min_index] < posc:
            print("LEFT")
        else:
            print("RIGHT")
        return
    
    # check other rows, then move
    other_rows_w_ds = [r for r in range(num_r) if ('d' in board[r] and r != posr)]
    if len(other_rows_w_ds) > 0:
        dists = [r - posr for r in other_rows_w_ds]
        min_index = dists.index(min(dists))
        if other_rows_w_ds[min_index] < posr:
            print("UP")
        else:
            print("DOWN")
        return
    
# Tail starts here

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)