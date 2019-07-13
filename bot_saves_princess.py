#!/usr/bin/python

def findPrincess(n, grid):
    coord_list = [(0, 0), (0, n-1), (n-1, 0), (n-1, n-1)]
    for coord in coord_list:
        if grid[coord[0]][coord[1]] == 'p':
            return (coord[0], coord[1])

def findBot(n, grid):
    for y_idx in range(n):
        row = grid[y_idx]
        m_pos = [p for p in range(n) if row[p] == 'm']
        if len(m_pos) == 1:
            return (y_idx, m_pos[0])

def displayPathtoPrincess(n,grid):
    # get bot position
    m_y, m_x = findBot(n, grid)
    # get princess position
    p_y, p_x = findPrincess(n, grid)
    
    v_move = p_y - m_y
    h_move = p_x - m_x
    
    moves = ""
    while v_move != 0:
        if v_move < 0:
            moves += 'UP\n'
            v_move += 1
        elif v_move > 0:
            moves += 'DOWN\n'
            v_move -= 1
    
    while h_move != 0:
        if h_move < 0:
            moves += 'LEFT\n'
            h_move += 1
        elif h_move > 0:
            moves += 'RIGHT\n'
            h_move -= 1
    
    print(moves)

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)