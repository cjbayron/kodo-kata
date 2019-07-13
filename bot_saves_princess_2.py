#!/usr/bin/python

def findPrincess(n, grid):
    for y_idx in range(n):
        row = grid[y_idx]
        m_pos = [p for p in range(n) if row[p] == 'p']
        if len(m_pos) == 1:
            return (y_idx, m_pos[0])

def nextMove(n,r,c,grid):
    # get princess position
    p_y, p_x = findPrincess(n, grid)
    
    v_move = p_y - r
    h_move = p_x - c
    
    if v_move < 0:
        return "UP"
    elif v_move > 0:
        return "DOWN"
    
    if h_move < 0:
        return "LEFT"
    elif h_move > 0:
        return "RIGHT"
    
n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))